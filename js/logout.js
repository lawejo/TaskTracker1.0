function userLogout() {
    fetch('/logout', {
    method: 'POST',
    })

    window.location.href = '/'

    closeLogout()
    
}