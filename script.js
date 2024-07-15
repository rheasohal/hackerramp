document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var form = this;
    var url = form.getAttribute('action');

    var formData = new FormData(form);
    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Update results div with data
        var resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
