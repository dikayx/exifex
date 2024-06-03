# ExifEx

ExifEx is a small utility tool to extract EXIF metadata from images. It is written in Python and Flask and uses the Pillow library to read the images and retrieve the metadata.

![Screenshot of the app](res/screenshot.png)

_Example images taken from [this](https://github.com/ianare/exif-samples) repository._

## Features

-   🏞️ Extract EXIF metadata from images (_JPEG, PNG, TIFF, GIF, WebP, and more comming soon!_)
-   🕵️‍♀️ Display the metadata and GPS coordinates in a human-readable format
-   🌍 Generate a Google Maps link to the location where the image was taken (if available)
-   🗂️ Supports multiple images at once
-   🔒 No data is stored on the server

## Get started

<!-- TODO: Add link to hosted website once it's available -->

The easiest way is to use the website hosted on Vercel. You can access it on [here (TODO)](README).

However, if you want to run the app locally, you can follow the [installation instructions](#installation) below.

### Usage

It's simple! Just drag and drop one or multiple image file into the dropzone or click on it to select a file from your computer. The app will then display the extracted metadata and GPS coordinates (if available).

> **⚠️ Note**: Exif data can contain sensitive information, such as the location where the image was taken. Only analyze images you have the right to use.

## Installation

You can either run the app directly on your machine or use Docker to run it in a container.

### Local

ExifEx requires Python 3.11 or higher to run locally.

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
    - To change the port or set the host, use the `-p` and `-b` flags respectively (e.g. `python3 src/app.py -b 0.0.0.0 -p 8080`)

_\*) You might need to use python and pip instead of python3 and pip3 depending on your system._

### Docker

You can also run the app using Docker and the `Dockerfile` provided in the repository.

1. Build the Docker image

    ```bash
    docker build -t exifex .
    ```

2. Run the Docker container

    ```bash
    docker run -p 8080:8080 exifex
    ```

You can also use the `docker-compose.yml` file to run the app. Just run `docker-compose up` after you built the image and the app will be available on `http://localhost:8080`.

1. Clone the repository

    ```bash
    git clone https://github.com/dan-koller/exifex
    cd exifex
    ```

2. Run the app using Docker Compose

    ```bash
    docker-compose up
    ```

3. Access the app on `http://localhost:8080`

4. Stop the app using `Ctrl+C` and run `docker-compose down` to remove the containers
