async function editTask() {
  const frm = event.target;
  const frmData = frm.parentElement.previousElementSibling;
  const editTaskModal = document.querySelector("#editTaskModal");

  const conn = await fetch("api-edit-task", {
    method: "PUT",
    body: new FormData(frmData),
  });
  const data = await conn.json();
  console.log(data);
  // Failure
  if (!conn.ok) {
    console.log("Cannot update");

    return;
  } else if (conn.ok) {
    location.href = `/dashboard`;
  }
}
