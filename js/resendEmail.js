"use strict"
const feedbackElement = document.querySelector('.feedback-element');

async function resendEmailAsync() {
    console.log(`aa`);
    const frm = event.target;
    console.log(frm);
    const response = await fetch("/api-resend-email", {
        method: "POST",
        body: new FormData(frm)
    });
    const data = await response.json();
    console.log(data);
    data.info === 'ok' ? succes() : error();
    function succes() {

        feedbackElement.parentElement.classList.contains('bg-red-600') ? feedbackElement.parentElement.classList.remove('bg-red-600') : ''
        feedbackElement.parentElement.classList.add('bg-green-500');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.message
        setTimeout(() => { location.href = `/` }, 3000)
    }
    function error() {
        feedbackElement.parentElement.classList.add('bg-red-600');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.errortype

    }
}
const resendEmailElements = [...document.querySelectorAll('.reveal')]
function revealEmailInput() {
    resendEmailElements.forEach((el) => el.classList.remove('hidden'))
}

