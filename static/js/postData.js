let deleteForm = document.getElementById('delete-form')
let deleteButton = document.getElementById('delete-post-button')

async function postData(url = "", data = {}) {
  console.log('nsv')
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify(data),
    });
    return response.json();
}

deleteForm.addEventListener('submit', e => {
  e.preventDefault();
  postData('127.0.0.1:8000/deletePost', {'post-id': deleteForm.dataset.id});
}, true)

deleteButton.addEventListener('click', e => {
  e.preventDefault()
  postData('127.0.0.1:8000/deletePost', {'post-id': deleteForm.dataset.id});
})