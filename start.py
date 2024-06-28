import argparse

from exifex import app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ExifEx - Extract meta data from images")
    parser.add_argument("-d", "--debug", action="store_true", default=False,
                        help="Enable debug mode")
    parser.add_argument("-b", "--bind", default="127.0.0.1", type=str,
                        help="Specify the bind address (default: 127.0.0.1)")
    parser.add_argument("-p", "--port", default=8080, type=int,
                        help="Specify the port (default: 8080)")

    args = parser.parse_args()

    web_app = app.create_app()
    web_app.run(debug=args.debug, host=args.bind, port=args.port)
