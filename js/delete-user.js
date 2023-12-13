"use strict"
let deleteUserModal;

async function deleteUser() {
    const frm = event.target // the form
    const conn = await fetch("/api-delete-user", { method: "DELETE", body: new FormData(frm) })
    const data = await conn.json() // to get plain text
    data.info == 'ok' ? success() : error();

    function success() {
        closeDeleteUserModal()
        // #TODO: Tilføj error handling4
        // #TODO: Fjern html element

    }
    function error() {
        console.log(`error handling`);
    }
}

function openDeleteUserModal() {
    deleteUserModal = event.target.previousElementSibling.previousElementSibling
    deleteUserModal.classList.remove('hidden')
    const userId = event.target.value
}
function closeDeleteUserModal() {
    deleteUserModal.classList.add("hidden")
}