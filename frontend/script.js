document.getElementById('upload-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const formData = new FormData();
    const fileInput = document.getElementById('file-input').files[0];
    const urlInput = document.getElementById('url-input').value;

    if (fileInput) {
        formData.append('file', fileInput);
    } else if (urlInput) {
        formData.append('url', urlInput);
    } else {
        alert('Please upload a file or enter a URL.');
        return;
    }

    try {
        // Send the form data to the backend via fetch API
        const response = await fetch('/scan', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            // Assuming the backend returns the scan result, open a new screen with the result
            const result = await response.json();

            // Redirect to a new screen and pass the result
            const resultPageUrl = '/result'; // Assuming you have a result route set up
            window.location.href = `${resultPageUrl}?data=${encodeURIComponent(JSON.stringify(result))}`;
        } else {
            alert('Error occurred during scanning.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while scanning.');
    }
});

// Remove file input when the "Remove File" button is clicked
document.getElementById('remove-file-button').addEventListener('click', function() {
    const fileInput = document.getElementById('file-input');
    fileInput.value = ''; // Clear the file input
    alert('File removed. You can select a new file.');
});
