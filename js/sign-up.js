"use strict"
const errorElement = document.querySelector('.error-element');
async function submitSignUp() {

    const frm = event.target // the form
    const conn = await fetch("/api-sign-up", {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json() // to get plain text
    console.log(data);
    data.info === 'ok' ? succes() : error();
    function succes() {
        console.log(`succes`);
    }
    function error() {
        console.log(`error`);
        errorElement.innerHTML = data.errortype
    }



};