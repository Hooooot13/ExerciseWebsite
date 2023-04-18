const editor = document.querySelector('.editor');
document.querySelectorAll('button').forEach(button => {
  button.addEventListener('click', async e => {
    const request = await fetch(`/exercises/${button.dataset.rowId}`);
    const exercise = await request.text();
    
    editor.innerHTML = exercise;

    const CSRFToken = document.head.querySelector('meta[name=csrf-token]').content;

    editor.querySelectorAll('[data-input-name]').forEach(submitter => {
      submitter.addEventListener('click', e => {
        const update = submitter
          .parentElement
          .querySelector(`[name="${submitter.dataset.inputName}"]`)
          .value;

        fetch(
          `/exercises/${button.dataset.rowId}`,
          {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRF-Token': CSRFToken
            },
            body: `{"${submitter.dataset.inputName}": "${update}"}`
          }
        ).then(response => {
          if (response.status === 204) location.reload();
        })
      })
    })
  })
})
