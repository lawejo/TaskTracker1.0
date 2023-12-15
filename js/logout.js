"use strict"

async function logout() {
    console.log(`logout`);
    const conn = await fetch("/logout", {
        method: "GET",
    })
    const data = await conn.json() // to get plain text

    data.info === "ok" ? succes() : error();

    function succes() {
        setTimeout(() => { location.href = `/` }, 1500)

    }
    function error() {
        console.log(data.message);
    }
    // function userLogout() {
    //     fetch('/logout', {
    //     method: 'POST',
    //     })

    //     window.location.href = '/'

    //     closeLogout()

}