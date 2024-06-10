// Used to handle the file upload functionality when
// an error message is displayed on the page, so the
// user can seemlessly upload files again.
document.addEventListener("DOMContentLoaded", function () {
    initializeFileUpload();
});

function initializeFileUpload() {
    const dragDropArea = document.getElementById("dragDropArea");
    const fileInput = document.getElementById("fileInput");

    const MAX_FILES = 16; // Files at once
    const MAX_CONTENT_LENGTH = 100 * 1024 * 1024; // 10MB per file

    const allowedTypes = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/webp",
        "image/tiff",
    ];

    if (!dragDropArea || !fileInput) {
        return;
    }

    dragDropArea.addEventListener("click", () => {
        fileInput.click();
    });

    dragDropArea.addEventListener("dragover", (event) => {
        event.preventDefault();
        dragDropArea.classList.add("bg-light");
    });

    dragDropArea.addEventListener("dragleave", () => {
        dragDropArea.classList.remove("bg-light");
    });

    dragDropArea.addEventListener("drop", (event) => {
        event.preventDefault();
        dragDropArea.classList.remove("bg-light");
        const files = event.dataTransfer.files;
        handleFiles(files);
    });

    fileInput.addEventListener("change", () => {
        const files = fileInput.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        if (files.length === 0) {
            return;
        }

        /* --------------- Limitations --------------- */
        // Remove the following code block, if you don't
        // want to limit the number of files that can be
        // uploaded at once.
        if (files.length > MAX_FILES) {
            alert("You can only upload up to 16 files at once.");
            return;
        }
        /* ------------------------------------------- */

        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
            // Image must not exceed 10MB
            if (files[i].size > MAX_CONTENT_LENGTH) {
                alert("File size must be less than 10MB");
                return;
            }
            // Only support image files (JPEG, PNG, GIF, WEBP, TIFF)
            if (!allowedTypes.includes(files[i].type)) {
                alert("Invalid file type. Please upload an image file.");
                return;
            }
            formData.append("images", files[i]);
        }

        fetch("/", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.text()) // Expecting an HTML response
            .then((html) => {
                document.open();
                document.write(html);
                document.close();
                initializeFileUpload(); // Re-initialize the file upload listeners after the DOM update
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }
}
