async function createTask() {
  const frm = event.target;
  const conn = await fetch("/api-create-task", {
    method: "POST",
    body: new FormData(frm),
  });
  // Failure
  if (!conn.ok) {
    console.log("Cannot update");

    return;
  } else if (conn.ok) {
    location.href = `/dashboard`;
  }
  const data = await conn.json();
  console.log(data);
  const cookie = data.cookie;

  document.querySelector("#tasks").insertAdjacentElement(
    "afterbegin"`
  <div id="tasks">
  <div
    class="p-4 rounded-md placeholder-content w-72 task-container bg-primary font-montserrat tasks"
  >
    <div class="">
      <p class="text-xs text-detail">${data.task_created_at}</p>
      <h3 class="my-2 text-secondary text-h4">${data.task_title}</h3>
      <p class="text-text">${data.task_description}</p>
      <div class="flex items-center justify-end gap-2 mt-4">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
        >
          <path
            fill="#b9b5d4"
            d="m10.95 13.7l-1.425-1.425q-.3-.3-.7-.3t-.7.3q-.3.3-.3.713t.3.712l2.125 2.15q.3.3.7.3t.7-.3l4.25-4.25q.3-.3.3-.712t-.3-.713q-.3-.3-.712-.3t-.713.3L10.95 13.7ZM12 22q-1.875 0-3.512-.712t-2.85-1.925q-1.213-1.213-1.925-2.85T3 13q0-1.875.713-3.512t1.924-2.85q1.213-1.213 2.85-1.925T12 4q1.875 0 3.513.713t2.85 1.925q1.212 1.212 1.925 2.85T21 13q0 1.875-.712 3.513t-1.925 2.85q-1.213 1.212-2.85 1.925T12 22Zm0-9ZM2.05 7.3q-.275-.275-.275-.7t.275-.7L4.9 3.05q.275-.275.7-.275t.7.275q.275.275.275.7t-.275.7L3.45 7.3q-.275.275-.7.275t-.7-.275Zm19.9 0q-.275.275-.7.275t-.7-.275L17.7 4.45q-.275-.275-.275-.7t.275-.7q.275-.275.7-.275t.7.275l2.85 2.85q.275.275.275.7t-.275.7ZM12 20q2.925 0 4.963-2.037T19 13q0-2.925-2.037-4.962T12 6Q9.075 6 7.038 8.038T5 13q0 2.925 2.038 4.963T12 20Z"
          />
        </svg>
        <p class="text-text">${data.task_due_date}</p>
      </div>
    </div>
  </div>
</div>
  `
  );
}

// Function to sort tasks by status
function sortTasksByStatus(status) {
  const taskContainers = document.querySelectorAll(".task-container");

  taskContainers.forEach((container) => {
    const taskStatus = container
      .querySelector(".task_status")
      .textContent.trim();

    if (taskStatus.toLowerCase() === status.toLowerCase()) {
      container.style.display = "block";
    } else {
      container.style.display = "none";
    }
  });
}
const selectInput = document.querySelector('select[name="task_status"]');
selectInput.addEventListener("change", (event) => {
  const selectedStatus = event.target.value;
  sortTasksByStatus(selectedStatus);
});
