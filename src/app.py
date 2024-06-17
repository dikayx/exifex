import argparse
import base64
import os
from config import Config
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from utils import extract_gps_info, format_coordinates


# --------------- App Configuration ----------------- #
app = Flask(__name__)
app.name = "ExifEx"
app.secret_key = os.urandom(24)
app.config.from_object(Config)

# --------------- Helper Functions ----------------- #
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# --------------- Routes ----------------- #
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    
    images = request.files.getlist('images')
    if app.config['MAX_FILES'] and len(images) > app.config['MAX_FILES']:
        return render_template('index.html', error=f"Only {app.config['MAX_FILES']} images are allowed at a time.")
    
    data = []
    for image in images:
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            file_size = len(image.read())
            image.seek(0)  # Reset file pointer to the beginning after reading for size

            if app.config['MAX_SIZE'] and file_size > app.config['MAX_CONTENT_LENGTH']:
                return render_template('index.html', error=f"{filename} is too large! Maximum size is {app.config['MAX_SIZE']} MB.")

            encoded_image = base64.b64encode(image.read()).decode('utf-8')
            image.seek(0)  # Reset file pointer again for reading image content
            
            meta_data = extract_gps_info(image)
            f_gps_coords = format_coordinates(meta_data.get("gps_coords")) if meta_data.get("gps_coords") else None
            data.append({
                'file': f"data:{image.content_type};base64,{encoded_image}",
                'filename': filename,
                'content_type': image.content_type,
                'exif_data': meta_data["exif_data"],
                'gps_coords': f_gps_coords,
                'maps_url': meta_data.get("maps_url")
            })
        else:
            return render_template('index.html', error=f"Invalid file type: {filename}.")
        
    return render_template('index.html', data=data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ExifEx - Extract meta data from images")
    parser.add_argument("-d", "--debug", action="store_true", default=False,
                        help="Enable debug mode")
    parser.add_argument("-b", "--bind", default="127.0.0.1", type=str,
                        help="Specify the bind address (default: 127.0.0.1)")
    parser.add_argument("-p", "--port", default=8080, type=int,
                        help="Specify the port (default: 8080)")
    parser.add_argument("--no-limits", action="store_true", default=False,
                        help="Disable the file count and size limits")

    args = parser.parse_args()

    # TODO: Find a better way to handle this
    if args.no_limits:
        app.config['MAX_FILES'] = 0
        app.config['MAX_SIZE'] = 0

    app.config['MAX_CONTENT_LENGTH'] = app.config['MAX_SIZE'] * 1024 * 1024 if app.config['MAX_SIZE'] > 0 else None

    app.run(debug=args.debug, host=args.bind, port=args.port)
