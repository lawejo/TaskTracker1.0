async function deleteTask() {
  const frm = event.target;
  console.log(frm);
  const conn = await fetch("api-delete-task", {
    method: "DELETE",
    body: new FormData(frm),
  });

  const data = await conn.json();
  console.log(data);
  console.log(frm.closest(".tasks"));

  frm.closest(".tasks").remove();
}
