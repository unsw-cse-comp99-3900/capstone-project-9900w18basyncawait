document.getElementById('trainButton').addEventListener('click', function() {
    var files = document.getElementById('fileUpload').files;
    if (files.length === 0) {
        alert('Please select a file!');
        return;
    }

    var formData = new FormData();
    for (var i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
    }

    console.log('Files selected:', files);

    fetch('http://localhost:5000/train', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Server response:', data);
        if (data.images && data.images.length === 4) {
            document.getElementById('resultImage1').src = 'http://localhost:5000' + data.images[0];
            document.getElementById('resultImage2').src = 'http://localhost:5000' + data.images[1];
            document.getElementById('resultImage3').src = 'http://localhost:5000' + data.images[2];
            document.getElementById('resultImage4').src = 'http://localhost:5000' + data.images[3];
            document.getElementById('result').style.display = 'block';
        } else {
            alert('Server did not return the expected number of images.');
        }
    })
    .catch(error => {
        console.error('Error uploading files:', error);
        alert('Failed to upload files.');
    });
});
