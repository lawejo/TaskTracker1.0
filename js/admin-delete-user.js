"use strict"
let deleteUserModal;
const feedbackElement = document.querySelector('.feedback-element');


async function deleteUser() {
    const frm = event.target // the form
    const userInfoParentEl = document.querySelector(`#delete-user-parent-${frm[0].value}`)
    const conn = await fetch("/api-delete-user", { method: "DELETE", body: new FormData(frm) })
    const data = await conn.json() // to get plain text
    data.info == 'ok' ? success() : error();

    function success() {
        closeDeleteUserModal()
        userInfoParentEl.remove()
        feedbackElement.parentElement.classList.contains('bg-red-600') ? feedbackElement.parentElement.classList.remove('bg-red-600') : ''
        feedbackElement.parentElement.classList.add('bg-green-500');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.message
        setTimeout(() => { feedbackElement.classList.add('hidden') }, 1500)
    }
    function error() {
        feedbackElement.parentElement.classList.add('bg-red-600');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.errortype
    }
}

function openDeleteUserModal() {
    deleteUserModal = event.target.closest('div').children[1]
    deleteUserModal.classList.remove('hidden')
}
function closeDeleteUserModal() {
    deleteUserModal.classList.add("hidden")
}