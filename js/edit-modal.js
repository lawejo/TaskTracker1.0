function openTaskModal(button) {
  const modal = document.getElementById("editTaskModal");
  modal.classList.remove("hidden");

  const taskContainer = button.closest(".task-container");
  const taskId = document.querySelector(".task_id").value;
  const taskTitle = taskContainer.querySelector(".text-secondary").textContent;
  const taskDueDate = document.querySelector(".task_due_date").textContent;
  const taskDescription = taskContainer.querySelector(".text-text").textContent;

  console.log(taskId);
  // const modalTitle = modal.querySelector("h2");
  // console.log(modal.firstChild.firstChild);
  // modalTitle.textContent = taskTitle;

  const editTaskForm = document.getElementById("editTaskForm");
  editTaskForm.innerHTML = `
          <input
          type="hidden"
          class="task_id"
          name="task_id"
          value="${taskId}"
        />
        <input
          type="text"
          name="task_title"
          placeholder="Task Title"
          value="${taskTitle}"
          class="block w-full px-3 py-2 mb-3 bg-transparent border rounded border-[#6D6D6D] placeholder-[#D9D9D9] text-secondary"
        />
        <textarea
          name="task_description"
          placeholder="Task Description"
          class="block w-full px-3 py-2 mb-3 bg-transparent border rounded border-[#6D6D6D] placeholder-[#D9D9D9] text-secondary"
        >${taskDescription}</textarea>
        <input
          type="date"
          name="task_due_date"
          placeholder="Due Date"
          value="${taskDueDate}"
          class="block w-full px-3 py-2 mb-3 bg-transparent border rounded border-[#6D6D6D] placeholder-[#D9D9D9] text-secondary"
        />
        <select
          name="task_status"
          class="block w-full px-3 py-2 mb-3 bg-transparent border rounded border-[#6D6D6D] placeholder-[#D9D9D9] text-secondary"
        >
          <option value="todo">To Do</option>
          <option value="inprogress">In Progress</option>
          <option value="done">Done</option>
        </select>
      `;
}

function closeTaskModal() {
  const modal = document.getElementById("editTaskModal");
  modal.classList.add("hidden");
}
