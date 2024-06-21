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

However, if you want to run the app locally, simply use the [setup.sh](setup.sh) script to set up the app on your machine or take a look at the [installation guide](docs/INSTALLATION.md) for more detailed instructions.

### Usage

It's simple! Just drag and drop one or multiple image file into the dropzone or click on it to select a file from your computer. The app will then display the extracted metadata and GPS coordinates (if available).

> **⚠️ Note**: Exif data can contain sensitive information, such as the location where the image was taken. Only analyze images you have the right to use.

### Limitations

By default, there are limitations to the file size and the number of images you can analyze at once when running the app locally or accessing it on Vercel. These values are set to **8 images at once** and **10 MB** due to the limitations of the free tier of Vercel. To customize these values, take a look at the [configuration guide](docs/CONFIGURATION.md).

_When running the app using Docker, the limitations are disabled by default. The setup script will also ask you if you want to disable the limitations._

## Contributing

If you want to contribute to the project, feel free to open an issue or a pull request. You can also suggest new features or improvements by creating an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
