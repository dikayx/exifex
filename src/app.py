from flask import Flask, render_template, request
import base64
from utils import extract_gps_info

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
        data.append({
            'file': f"data:{image.content_type};base64,{encoded_image}",
            'filename': image.filename,
            'content_type': image.content_type,
            'exif_data': meta_data["exif_data"],
            'gps_coords': meta_data["gps_coords"],
            'maps_url': meta_data.get("maps_url")
        })
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
