// Get the modal and buttons
const taskModal = document.getElementById("taskModal");
const openModalBtn = document.getElementById("openModal");
const closeModalBtn = document.getElementById("closeModal");
const taskForm = document.getElementById("taskForm");

// Function to open the modal
function openModal() {
  taskModal.classList.remove("hidden");
}

// Function to close the modal
function closeModal() {
  taskModal.classList.add("hidden");
}

// Event listeners to handle modal functionality
openModalBtn.addEventListener("click", openModal);
closeModalBtn.addEventListener("click", closeModal);
taskForm.addEventListener("submit", (event) => {
  // Logic to handle task creation goes here
  // Prevent form submission for demo purposes
  event.preventDefault();
  closeModal();
});
