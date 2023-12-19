"use strict"
console.log(`1`);
const url = window.location
const target = document.querySelector(".loginB")
if (url.pathname === '/dashboard' && target) {
    target.insertAdjacentHTML("afterbegin", `
    <button id="openModal">
    <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 20 20">
    <path fill="#c6c5c7"
    d="M18 10a8 8 0 1 1-16 0a8 8 0 0 1 16 0ZM6 10a.5.5 0 0 0 .5.5h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0-.5.5Z" />
    </svg>
    </button>
    `)
} 
