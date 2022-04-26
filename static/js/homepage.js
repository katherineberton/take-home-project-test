// prefaces the login form

const loginForm = document.querySelector('#login-form');
loginForm.insertAdjacentHTML('beforebegin', '<p>Log in with your email address here:</p>');


// reads content of the text input in real time

const loginInput = document.querySelector('#login-email');
var email;

loginInput.addEventListener('input', () => {
    email = loginInput.value;
    console.log(email)
})