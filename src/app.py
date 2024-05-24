import argparse
import base64
from flask import Flask, render_template, request
from utils import extract_gps_info, format_coordinates


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    
    # Get the image(s), can be multiple
    images = request.files.getlist('images')
    data = []
    for image in images:
        encoded_image = base64.b64encode(image.read()).decode('utf-8')
        meta_data = extract_gps_info(image)
        # Only format the coordinates if they exist
        f_gps_coords = format_coordinates(meta_data["gps_coords"]) if "gps_coords" in meta_data and meta_data["gps_coords"] else None
        data.append({
            'file': f"data:{image.content_type};base64,{encoded_image}",
            'filename': image.filename,
            'content_type': image.content_type,
            'exif_data': meta_data["exif_data"],
            'gps_coords': f_gps_coords,
            'maps_url': meta_data.get("maps_url")
        })
    return render_template('index.html', data=data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ExifEx - Extract meta data from images")
    parser.add_argument("-d", "--debug", action="store_true", default=False,
                        help="Enable debug mode")
    parser.add_argument("-b", "--bind", default="127.0.0.1", type=str)
    parser.add_argument("-p", "--port", default="5000", type=int)
    args = parser.parse_args()

    app.run(debug=args.debug, host=args.bind, port=args.port)
