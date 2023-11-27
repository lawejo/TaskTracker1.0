async function createTask() {
  const frm = event.target;
  const conn = await fetch("/api_create_task", {
    method: "POST",
    body: new FormData(frm),
  });
  const data = await conn.json();
  const cookie = data.cookie;
}
