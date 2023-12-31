"use strict"
const feedbackElement = document.querySelector('.feedback-element');
async function login() {

    const frm = event.target // the form
    const conn = await fetch("/api-login", {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json() // to get plain text
    data.info === 'ok' ? succes() : error();
    function succes() {

        feedbackElement.parentElement.classList.contains('bg-red-600') ? feedbackElement.parentElement.classList.remove('bg-red-600') : ''
        feedbackElement.parentElement.classList.add('bg-green-500');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.message
        setTimeout(() => { location.href = `/dashboard` }, 1500)
    }
    function error() {
        feedbackElement.parentElement.classList.add('bg-red-600');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.errortype

    }



};