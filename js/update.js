const modalUpdate = document.getElementById("modal-update")

    function updateModal() {
        modalUpdate.classList.remove("hidden")
        document.body.style.overflow = "hidden";
        window.addEventListener("click", function(event) {
            if (event.target === modalUpdate) {
                closeUpdateModal()
            }
        })
    }

    function closeUpdateModal() {
        modalUpdate.classList.add("hidden")
        document.body.style.overflow = "scroll";
    }


    async function update() {
        let user_firstname = document.querySelector("input[name='userfirstname_update']").value;
        let user_lastname = document.querySelector("input[name='userlastname_update']").value;
        const avatar = document.querySelector("input[name='avatar_update']").files[0];
        const formData = new FormData();
        const regex = /^[a-zA-Z-9_]*$/;
    
        if (user_firstname === "" || regex.test(user_firstname)) {
            formData.append('user_firstname', user_firstname);
        }
        
        if (user_lastname === "" || regex.test(user_lastname)) {
            formData.append('user_lastname', user_lastname);
        }
    
        if (avatar) {
            formData.append('avatar', avatar);
        }
    
        if ((user_firstname && !regex.test(user_firstname)) || (user_lastname && !regex.test(user_lastname))) {
            const errorMessageFirstname = document.getElementById("errorMessageFirstname");
            errorMessageFirstname.classList.remove("hidden");
            errorMessageFirstname.classList.add("flex");
            const errorMessageLastname = document.getElementById("errorMessageLastname");
            errorMessageLastname.classList.remove("hidden");
            errorMessageLastname.classList.add("flex");
            
        } else {
            const response = await fetch("/update", {
                method: "PUT",
                body: formData
            });
            const data = await response.json();
            closeUpdateModal();
            if (!user_firstname) {
                user_firstname = data.new_user_firstname;
            }
            if (!user_lastname) {
                user_lastname = data.new_user_lastname;
            }
            window.location.href = "/profile";
        }
    }
    