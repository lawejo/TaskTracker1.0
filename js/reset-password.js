const passwordInput = document.getElementById("passwordInput")
const emailInput = document.getElementById("emailInput")
function showResetPassword() {
    const resetEmailButton = document.getElementById("resetEmailButton")
    resetEmailButton.classList.remove("hidden")
    passwordInput.classList.remove("hidden")
    emailInput.classList.remove("hidden")
}

async function resetPassword() {
    const password = passwordInput.value
    const email = emailInput.value
    const formData = new FormData();
    formData.append('user_password', password);
    formData.append('user_email', email);

    const response = await fetch("/reset-password", {
        method: "POST",
        body: formData
    })

    const data = await response.json()
}