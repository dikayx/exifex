# --------------- Configuration ----------------- #
# If you don't want to limit the number of images
# or the size of each image, set the values to 0.
# ---------------------------------------------- #
class Config:
    MAX_FILES = 8 # Images at a time
    MAX_SIZE = 10 # MB per image
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp', 'tiff'}

    @staticmethod
    def init_app(app):
        pass
