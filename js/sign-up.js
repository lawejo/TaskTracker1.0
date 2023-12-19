"use strict"
const feedbackElement = document.querySelector('.feedback-element');
async function submitSignUp() {

    const frm = event.target // the form
    const conn = await fetch("/api-sign-up", {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json() // to get plain text
    data.info === 'ok' ? succes() : error();
    function succes() {
        feedbackElement.parentElement.classList.add('bg-green-500');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.message
    }
    function error() {
        feedbackElement.parentElement.classList.add('bg-red-600');
        feedbackElement.parentElement.classList.remove('hidden');
        if (data.errortype === "UNIQUE constraint failed: users.user_email") {
            feedbackElement.innerHTML = "Email already in use. Try another"

        } else {
            feedbackElement.innerHTML = data.errortype
        }
    }


    1
};