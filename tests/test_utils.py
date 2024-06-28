import pytest

from io import BytesIO
from PIL import Image

from exifex.utils import extract_gps_info, format_coordinates, dms_to_string, convert_decimal_degrees, create_google_maps_url


# Test dms_to_string function
def test_dms_to_string():
    assert dms_to_string((40, 30, 20.123)) == '40.0° 30.0\' 20.12"'
    assert dms_to_string((0, 0, 0)) == '0.0° 0.0\' 0.00"'
    assert dms_to_string((90, 59, 59.999)) == '90.0° 59.0\' 60.00"'

# Test format_coordinates function
def test_format_coordinates():
    data = {
        'lat_ref': 'N',
        'lat': (40, 30, 20.123),
        'lon_ref': 'W',
        'lon': (80, 45, 15.456)
    }
    expected_output = "Latitude: 40.0° 30.0' 20.12\" N, Longitude: 80.0° 45.0' 15.46\" W"
    assert format_coordinates(data) == expected_output

# Test convert_decimal_degrees function
def test_convert_decimal_degrees():
    assert convert_decimal_degrees(40, 30, 20.123, 'N') == pytest.approx(40.5055897, rel=1e-6)
    assert convert_decimal_degrees(80, 45, 15.456, 'W') == pytest.approx(-80.7542933, rel=1e-6)
    assert convert_decimal_degrees(0, 0, 0, 'E') == 0.0
    assert convert_decimal_degrees(90, 0, 0, 'S') == -90.0

# Test create_google_maps_url function
def test_create_google_maps_url():
    gps_coords = {
        "lat": (40, 30, 20.123),
        "lat_ref": "N",
        "lon": (80, 45, 15.456),
        "lon_ref": "W"
    }
    expected_url = "https://maps.google.com/?q=40.505589722222226,-80.75429333333334"
    assert create_google_maps_url(gps_coords) == expected_url

# Mock image with EXIF data for testing extract_gps_info function
class MockImage:
    def __init__(self, exif_data):
        self.exif_data = exif_data

    def _getexif(self):
        return self.exif_data

def test_extract_gps_info(monkeypatch):
    # Mock the Image.open function to return a MockImage
    exif_data = {
        34853: {
            1: 'N',
            2: (40, 30, 20.123),
            3: 'W',
            4: (80, 45, 15.456)
        }
    }
    monkeypatch.setattr("PIL.Image.open", lambda file: MockImage(exif_data))

    gps_info = extract_gps_info(BytesIO(b"mock image data"))
    expected_gps_coords = {
        'lat': (40, 30, 20.123),
        'lat_ref': 'N',
        'lon': (80, 45, 15.456),
        'lon_ref': 'W'
    }
    assert gps_info['gps_coords'] == expected_gps_coords
    assert gps_info['maps_url'] == "https://maps.google.com/?q=40.505589722222226,-80.75429333333334"
