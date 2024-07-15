import base64

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from exifex.helpers import allowed_file
from exifex.utils import extract_gps_info, format_coordinates

blueprint = Blueprint("exifex", __name__)


# --------------- Routes ----------------- #
@blueprint.route('/', methods=['GET', 'POST'])
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
