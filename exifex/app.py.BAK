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

# -------------------- Routes ---------------------- #
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    
    images = request.files.getlist('images')
    
    data = []
    for image in images:
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            encoded_image = base64.b64encode(image.read()).decode('utf-8')
            image.seek(0) # Reset file pointer after reading
            
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

# ------------------- Main Block ------------------- #
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ExifEx - Extract meta data from images")
    parser.add_argument("-d", "--debug", action="store_true", default=False,
                        help="Enable debug mode")
    parser.add_argument("-b", "--bind", default="127.0.0.1", type=str,
                        help="Specify the bind address (default: 127.0.0.1)")
    parser.add_argument("-p", "--port", default=8080, type=int,
                        help="Specify the port (default: 8080)")

    args = parser.parse_args()

    app.run(debug=args.debug, host=args.bind, port=args.port)
