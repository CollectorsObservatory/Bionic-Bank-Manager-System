document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
    const errorMessage = document.getElementById('errorMessage');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const id = document.getElementById('id').value;
        const password = document.getElementById('password').value;

        if (id === 'admin' && password === '1234') {
            window.location.href = 'welcome.html';
        } else {
            errorMessage.style.display = 'block';
        }
    });
});
// Initiating ScrollReveal with basic parameters
const sr = ScrollReveal({
    origin: 'top',
    distance: '50px',
    duration: 1000,
    reset: true
});

// Basic animation for elements with the class .animate
sr.reveal('.animate', {
    interval: 200
});
