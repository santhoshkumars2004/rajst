document.getElementById('login-form').addEventListener('submit', function(event) {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username.trim() === '' || password.trim() === '') {
        event.preventDefault();
        document.getElementById('error-message').innerText = 'Please enter both username and password.';
    }
});
