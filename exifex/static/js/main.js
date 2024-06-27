// Used to handle the file upload functionality when
// an error message is displayed on the page, so the
// user can seemlessly upload files again.
document.addEventListener("DOMContentLoaded", function () {
    initializeFileUpload();
});

function initializeFileUpload() {
    const dragDropArea = document.getElementById("dragDropArea");
    const fileInput = document.getElementById("fileInput");

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

    // Little hack to prevent multiple alert dialogs
    if (!dragDropArea.classList.contains("initialized")) {
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

        dragDropArea.classList.add("initialized");
    }

    fileInput.addEventListener("change", () => {
        const files = fileInput.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        if (files.length === 0) {
            return;
        }

        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
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
