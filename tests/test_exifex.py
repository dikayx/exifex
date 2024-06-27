# Test if the index page is accessible
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

# Test if the title of the page is correct
def test_index_title(client):
    response = client.get('/')
    assert b'<title>\n            Exif Data Extractor | ExifEx\n        </title>' in response.data
