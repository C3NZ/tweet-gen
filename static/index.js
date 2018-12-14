function tellJoke() {
    fetch('/joke').then(function(response) {
        json = response.json()
        
        json.then(function(data) {
            document.getElementById('joke').innerText = data.joke;
            document.getElementById('punchline').innerText = data.punchline;
            document.querySelector('img').style = 'display: block; margin: auto;';
        });
    })
}
