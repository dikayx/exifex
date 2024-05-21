const dragDropArea = document.getElementById("dragDropArea");
const fileInput = document.getElementById("fileInput");

const allowedTypes = [
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/webp",
    "image/tiff",
];

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

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
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
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}
