
import React, { useEffect, useState } from "react";

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [editId, setEditId] = useState(null);
  const [completed, setCompleted] = useState(false);

  const API_URL = "http://127.0.0.1:8000/api/todos/";

  // read k liye
  const fetchTodos = async () => {
    const res = await fetch(API_URL);
    const data = await res.json();
    setTodos(data);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  // update k liye (create yahan nahi — sirf edit)
  const handleSubmit = async () => {
    if (!title || editId === null) return;

    await fetch(`${API_URL}${editId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title, completed }),
    });

    setEditId(null);
    setTitle("");
    setCompleted(false);
    fetchTodos();
  };

  // delete krne k liye
  const deleteTodo = async (id) => {
    await fetch(`${API_URL}${id}/`, {
      method: "DELETE",
    });
    fetchTodos();
  };

  // edit form k liye
  const editTodo = (todo) => {
    setTitle(todo.title);
    setEditId(todo.id);
    setCompleted(Boolean(todo.completed));
  };

  return (
    <div className="todo-card">
      <h1>Todo App</h1>

      <div className="todo-input">
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Edit a todo below, then click Update"
        />
        <button type="button" onClick={handleSubmit} disabled={editId === null}>
          Update
        </button>
      </div>
      <div>
      <ul className="todo-list">
        {todos.map((todo) => (
          <li key={todo.id}>
            <p>{todo.title}</p>

            <button onClick={() => editTodo(todo)}>Edit</button>

            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
      </div>
    </div>
  );
}

export default TodoApp;