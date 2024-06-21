# Configuration

By default, Exifex has some limitations to the file size and the number of images you can analyze at once. These values are set to **8 images at once** and **10 MB** due to the limitations of the free tier of Vercel and the fact that I don't want to deal with two code bases for hosting and local development.

## File Upload Limitations

You can change these limitations by modifying the `MAX_FILES` and `MAX_SIZE` variables in the [config.py](../src/config.py) and [main.js](../src/static/js/main.js) files. Set both values to `0` to remove the limitations.

> **⚠️ Note**: Increasing the limits can lead to performance issues and might cause the app to crash if the server runs out of memory.
