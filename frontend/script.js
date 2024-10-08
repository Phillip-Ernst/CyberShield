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

    const response = await fetch('/scan', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('results').innerHTML = `<pre>${JSON.stringify(result, null, 2)}</pre>`;
});