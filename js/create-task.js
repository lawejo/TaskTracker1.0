async function createTask() {
  const frm = event.target;
  const conn = await fetch("/api-create-task", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!conn.ok) {
    return;
  }

  const data = await conn.json();

  // Call the filterTask function after successful task creation
  await filterTask();

  const taskElement = document.createElement("div");
  taskElement.innerHTML = `
    <div class="p-4 rounded-md placeholder-content w-72 task-container bg-primary font-montserrat tasks">
      <div>
        <p class="text-xs text-detail">${data.task_created_at}</p>
        <h3 class="my-2 text-secondary text-h4">${data.task_title}</h3>
        <p class="text-text">${data.task_description}</p>
        <div class="flex items-center justify-end gap-2 mt-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
            <!-- SVG Path -->
          </svg>
          <p class="text-text">${data.task_due_date}</p>
        </div>
      </div>
    </div>
  `;

  const taskStatus = data.task_status;
  const tasksSection = document.getElementById(
    `task${taskStatus.charAt(0).toUpperCase() + taskStatus.slice(1)}`
  );
  tasksSection.appendChild(taskElement);
}

async function createTaskAndFilter() {
  const createdTask = await createTask();
  if (createdTask) {
    await filterTask();
  }
}
async function filterTask() {
  try {
    const filterTag = document.getElementById("filterTag").value;
    // Fetch tasks based on selected filter
    const conn = await fetch(`/filter_task?task_status=${filterTag}`, {
      method: "GET",
    });

    if (!conn.ok) {
      return;
    }

    const data = await conn.json();

    const taskToDoElement = document.getElementById("taskToDo");
    const taskInProgressElement = document.getElementById("taskInProgress");
    const taskDoneElement = document.getElementById("taskDone");

    // Append tasks to the respective sections based on their status
    data.results.forEach((task) => {
      // Assuming 'data.results' contains the tasks
      const taskElement = document.createElement("div");
      taskElement.classList.add(
        "p-4",
        "rounded-md",
        "placeholder-content",
        "w-72",
        "task-container",
        "bg-primary",
        "font-montserrat",
        "tasks"
      );

      taskElement.innerHTML = `
        <div>
          <p class="text-xs text-detail">${task.task_created_at}</p>
          <h3 class="my-2 text-secondary text-h4">${task.task_title}</h3>
          <p class="text-text">${task.task_description}</p>
          <div class="flex items-center justify-end gap-2 mt-4">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
              <!-- SVG Path -->
            </svg>
            <p class="text-text">${task.task_due_date}</p>
          </div>
        </div>
      `;

      if (task.task_status === "todo") {
        taskToDoElement.appendChild(taskElement);
      } else if (task.task_status === "inprogress") {
        taskInProgressElement.appendChild(taskElement);
      } else if (task.task_status === "done") {
        taskDoneElement.appendChild(taskElement);
      }
    });
  } catch (error) {
    console.error(error);
  }
}
