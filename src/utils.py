from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS


def create_google_maps_url(gps_coords):            
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees

def extract_gps_info( file):
    gps_data = {
        "file": file,
        "exif_data": {},
        "gps_coords": {}
    }
    
    try:
        image = Image.open(file)
        exif_data = image._getexif()
        
        if exif_data is None:
            print(f"{file} contains no exif data.")
        else:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag)
                if tag_name == "GPSInfo":
                    gps_info = {}
                    for key, val in value.items():
                        gps_tag_name = GPSTAGS.get(key)
                        gps_info[gps_tag_name] = val
                        if gps_tag_name == "GPSLatitude":
                            gps_data["gps_coords"]["lat"] = val
                        elif gps_tag_name == "GPSLongitude":
                            gps_data["gps_coords"]["lon"] = val
                        elif gps_tag_name == "GPSLatitudeRef":
                            gps_data["gps_coords"]["lat_ref"] = val
                        elif gps_tag_name == "GPSLongitudeRef":
                            gps_data["gps_coords"]["lon_ref"] = val
                    gps_data["exif_data"]["GPSInfo"] = gps_info
                else:
                    gps_data["exif_data"][tag_name] = value

            if gps_data["gps_coords"]:
                gps_data["maps_url"] = create_google_maps_url(gps_data["gps_coords"])

    except IOError:
        print(f"File format not supported for {file}!")
    
    return gps_data


# Export functions
__all__ = ['extract_gps_info']