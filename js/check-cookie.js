"use strict"
let count = 0;

let modalCount = 0
const sessionModal = document.querySelector('.renew-session')
const removeCookieForm = document.querySelector('#remove-cookie-forn')
async function updateCookie() {
    const frm = event.target;
    const response = await fetch("/renew-cookie", {
        method: "POST",
        body: new FormData(frm)
    });
    const data = await response.json(); count = 0
    closeRenewSession()
}
async function removeCookie() {
    const frm = removeCookieForm
    const response = await fetch("/remove-cookie", {
        method: "POST",
        body: new FormData(frm)
    });
    const data = await response.json();
    modalCount = 0
    window.location.reload();
}


function updateTimer() {
    count = count + 1;
    if (count >= 5 && sessionModal.classList.contains('hidden')) {
        sessionModal.classList.remove('hidden')
    } else if (count >= 10 && !sessionModal.classList.contains('hidden')) {
        removeCookie()
    }
}


setInterval(updateTimer, 60000);


function resetTimer() {
    !sessionModal.classList.contains('hidden') ? sessionModal.classList.add('hidden') : ''
    count = 0;

}
function closeRenewSession() {
    sessionModal.classList.add('hidden')
}
if (count < 5) {
    window.onload = resetTimer;
    window.onmousemove = resetTimer;
    window.onmousedown = resetTimer;
    window.ontouchstart = resetTimer;
    window.onclick = resetTimer;
    window.onkeypress = resetTimer;
}

