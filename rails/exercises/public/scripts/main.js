const editor = document.querySelector('.editor');
document.querySelectorAll('button').forEach(button => {
  button.addEventListener('click', async e => {
    const request = await fetch(`/exercises/${button.dataset.rowId}`);
    const exercise = await request.text();
    editor.innerHTML = exercise;
  })
})
