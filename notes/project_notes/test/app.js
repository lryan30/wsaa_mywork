async function loadTasks() {
    const res = await fetch('/api/tasks');
    const tasks = await res.json();
    const list = document.getElementById('task-list');
    list.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.innerText = `${task.title} (${task.status})`;
        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById('task-title');
    const title = input.value;
    if (!title) return;
    await fetch('/api/tasks', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title})
    });
    input.value = '';
    loadTasks();
}

loadTasks();
