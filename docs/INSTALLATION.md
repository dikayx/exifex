# Installation

ExifEx is a simple web app that allows you to view EXIF data from images. You can either run the app directly on your machine or use Docker to run it in a container.

This installation guide will show you how to set up the app locally or using Docker. You can also use the setup script provided in the repository to install the required dependencies and start the app.

## Local

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
    - To disable upload limits, add the `--no-limits` flag

_\*) You might need to use python and pip instead of python3 and pip3 depending on your system._

## Docker

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