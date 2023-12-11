"use strict"
async function deleteUser() {
    const frm = event.target // the form
    const conn = await fetch("/api-delete-user", { method: "DELETE", body: new FormData(frm) })
    const data = await conn.json() // to get plain text
    console.log(data);
} 