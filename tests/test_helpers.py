from exifex.helpers import allowed_file


# Test allowed file types
def test_allowed_file():
    assert allowed_file('image.jpg') == True
    assert allowed_file('image.jpeg') == True
    assert allowed_file('image.png') == True
    assert allowed_file('image.gif') == True
    assert allowed_file('image.webp') == True
    assert allowed_file('image.tiff') == True

# Test invalid file types
def test_invalid_file():
    assert allowed_file('image.txt') == False
    assert allowed_file('image.pdf') == False
    assert allowed_file('movie.mp4') == False