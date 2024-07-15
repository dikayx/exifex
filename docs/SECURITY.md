# Security

ExifEx aims to be a secure and privacy-friendly tool to extract EXIF metadata from images. To ensure the safety of the users, there are several security measures in place to protect against common vulnerabilities and threats. The main areas of focus are:

-   **CSRF protection**: ExifEx uses Flask-WTF to protect against Cross-Site Request Forgery (CSRF) attacks. This is done by generating a unique token for each submission and validating it on the server side. **Enabled by default**.

-   **Unique Session IDs**: Flask generates a unique session ID for each user session. This ID is used to store session data on the server and is regenerated after each request to prevent session fixation attacks. **Enabled by default**.

-   **SSL/TLS encryption**: ExifEx supports SSL/TLS encryption to secure the communication between the client and the server. This is especially important when handling sensitive data such as EXIF metadata. **Optional**.

    > **Note**: For development purposes, you can use a self-signed certificate with the `-a` flag to enable SSL. However, for production, you should use a valid SSL certificate. See the [installation guide](INSTALLATION.md#securing-the-app-with-ssl) for more information.

## Reporting Security Issues

If you discover a security issue in ExifEx, please [create an issue](https://github.com/dan-koller/exifex/issues). I take security seriously and will do my best to address the issue promptly.

If you have any contributions or suggestions to improve the security of ExifEx, feel free to open a pull request. Your help is greatly appreciated!
