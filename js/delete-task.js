async function deleteTask() {
  const frm = event.target;
  const conn = await fetch("api-delete-task", {
    method: "DELETE",
    body: new FormData(frm),
  });

  const data = await conn.json();


  frm.closest(".tasks").remove();
}
