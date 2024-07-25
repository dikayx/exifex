from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS


def dms_to_string(dms_tuple) -> str:
    """
    Converts a tuple of (degrees, minutes, seconds) to a formatted string.
    Used to convert GPS coordinates to a human-readable format.

    Parameters:
    - dms_tuple (tuple): A tuple containing degrees, minutes, and seconds.

    Returns:
    - str: A formatted string representing the degrees, minutes, and seconds.
    """
    degrees, minutes, seconds = map(float, dms_tuple)
    return f"{degrees:.1f}° {minutes:.1f}' {seconds:.2f}\""


def format_coordinates(data) -> str:
    """
    Creates a human-readable string from a dictionary containing latitude and longitude information.
    
    Parameters:
    - data (dict): A dictionary with keys 'lat_ref', 'lat', 'lon_ref', and 'lon'.
    
    Returns:
    - str: A formatted string representing the coordinates in a human-readable format.
    """
    lat_ref = data['lat_ref']
    lat = data['lat']
    lon_ref = data['lon_ref']
    lon = data['lon']

    lat_str = dms_to_string(lat)
    lon_str = dms_to_string(lon)

    return f"Latitude: {lat_str} {lat_ref}, Longitude: {lon_str} {lon_ref}"


def convert_decimal_degrees(degree, minutes, seconds, direction) -> float:
    """
    Convert GPS coordinates to decimal degrees. Used to create a Google Maps URL.

    Parameters:
    - degree (float): Degrees
    - minutes (float): Minutes
    - seconds (float): Seconds
    - direction (str): Direction (N, S, E, W)

    Returns:
    - float: Decimal degrees
    """
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees


def create_google_maps_url(gps_coords) -> str:
    """
    Create a Google Maps URL from GPS coordinates.

    Parameters:
    - gps_coords (dict): A dictionary containing GPS coordinates.

    Returns:
    - str: A URL to Google Maps with the GPS coordinates.
    """
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),
                                          float(gps_coords["lat"][1]),
                                          float(gps_coords["lat"][2]),
                                          gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),
                                          float(gps_coords["lon"][1]),
                                          float(gps_coords["lon"][2]),
                                          gps_coords["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"


def extract_gps_info(file) -> dict:
    """
    Extract GPS information from an image file.

    Parameters:
    - file: (Raw) image file as bytes.

    Returns:
    - dict: A dictionary containing the extracted GPS information.
    """
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
