"use strict"
const deleteUserModal = document.querySelector('.modal-delete-user')
async function deleteUser() {
    const frm = event.target // the form
    const conn = await fetch("/api-delete-user", { method: "DELETE", body: new FormData(frm) })
    const data = await conn.json() // to get plain text
    console.log(data);
}

function openDeleteUserModal() {
    deleteUserModal.classList.remove('hidden')

    const userId = event.target.value

    const userFirstName = document.querySelector(`.user_firstname_${userId}`).textContent
    console.log(userFirstName);
    const userLastName = document.querySelector(`.user_lastname_${userId}`).textContent
    console.log(userLastName);
    console.log(document.querySelector(`.username_${userId}`));
    document.querySelector(`.username_${userId}`).innerHTML = `${userFirstName}  ${userLastName}`
}
function closeDeleteUserModal() {
    deleteUserModal.classList.add("hidden")
}