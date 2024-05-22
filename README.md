# ExifEx

ExifEx is a small utility tool to extract EXIF metadata from images. It is written in Python and Flask and uses the Pillow library to read the images and retrieve the metadata.

## Get started

The easiest way is to use the website hosted on Vercel. You can access it on [here (TODO)](README).

However, if you want to run the app locally, follow the instructions below.

### Requirements

-   Python 3.11+
-   Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository

    ```bash
    git clone https://github.com/dan-koller/exifex
    ```

2. Create a new virtual environment & activate it

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

    > On Windows, open a command prompt and run `.venv\Scripts\activate.bat`

3. Install the required Python packages

    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the script you want to use

    ```bash
    python3 src/app.py
    ```

    - To run the app in debug mode, run `python3 src/app.py -d`
    - To change the port or set the host, use the `-p` and `-h` flags respectively (e.g. `python3 src/app.py -h 0.0.0.0 -p 8080`)

_\*) You might need to use python and pip instead of python3 and pip3 depending on your system._
