"use strict"
let editUserModal;

async function adminUpdateUser() {
    const frm = event.target;
    const response = await fetch("/api-admin-update-user", {
        method: "PUT",
        body: new FormData(frm)
    });
    const data = await response.json();
    const userData = data.user;
    const message = data.message
    data.info === 'ok' ? success() : error();
    function success() {
        const firstname = document.querySelector(`.user_firstname_${frm[0].value}`)
        const lastname = document.querySelector(`.user_lastname_${frm[0].value}`)
        firstname.innerHTML = userData.user_firstname
        lastname.innerHTML = userData.user_lastname
        closeEditUserModal()
        feedbackElement.parentElement.classList.contains('bg-red-600') ? feedbackElement.parentElement.classList.remove('bg-red-600') : ''
        feedbackElement.parentElement.classList.add('bg-green-500');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = message
        setTimeout(() => { feedbackElement.classList.add('hidden') }, 1500)
    }
    function error() {
        closeEditUserModal()
        feedbackElement.parentElement.classList.add('bg-red-600');
        feedbackElement.parentElement.classList.remove('hidden');
        feedbackElement.innerHTML = data.errortype
        setTimeout(() => { feedbackElement.classList.add('hidden') }, 3000)

    }
}
function openEditUserModal() {
    editUserModal = event.target.closest('div').children[2]
    editUserModal.classList.remove('hidden')
}
function closeEditUserModal() {
    editUserModal.classList.add("hidden")
}

