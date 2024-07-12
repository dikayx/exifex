import re


# Test if the index page is accessible
def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

# No other routes should be accessible
def test_404_page(client):
    response = client.get('/invalid')
    assert response.status_code == 404

# Test if the title of the page is correct
def test_index_title(client):
    response = client.get('/')
    title_regex = rb'<title>\s*Exif Data Extractor \| ExifEx\s*</title>'
    assert bool(re.search(title_regex, response.data))

# Test if the page contains the correct header
def test_index_header(client):
    response = client.get('/')
    header_regex = rb'<h5[^>]*>Drag and Drop Images Here</h5>'
    assert bool(re.search(header_regex, response.data))

# Test if there is an input field for file uploads
def test_index_input(client):
    response = client.get('/')
    input_regex = rb'<input[^>]*type="file"[^>]*>'
    assert bool(re.search(input_regex, response.data))

# Should not contain any exif data
def test_index_no_exif_data(client):
    response = client.get('/')
    exif_data_regex = rb'<div[^>]*class="exif-data"[^>]*>.*</div>'
    assert not bool(re.search(exif_data_regex, response.data))

# Should not contain any GPS coordinates
def test_index_no_gps_coords(client):
    response = client.get('/')
    gps_coords_regex = rb'<div[^>]*class="gps-coords"[^>]*>.*</div>'
    assert not bool(re.search(gps_coords_regex, response.data))

# Should not contain any error messages
def test_index_no_error(client):
    response = client.get('/')
    error_regex = rb'<div[^>]*class="alert"[^>]*>.*</div>'
    assert not bool(re.search(error_regex, response.data))

# Index page should contain a hidden input field for CSRF token
def test_index_csrf_token(client):
    response = client.get('/')
    csrf_token_regex = rb'<input[^>]*type="hidden"[^>]*name="csrf_token"[^>]*>'
    assert bool(re.search(csrf_token_regex, response.data))