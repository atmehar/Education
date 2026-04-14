
import React, { useEffect, useState } from "react";

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [editId, setEditId] = useState(null);

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

  // create or update k liye
  const handleSubmit = async () => {
    if (!title) return;

    if (editId === null) {
      // create k liey
      await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, completed: false }),
      });
    } else {
      // update k liye
      await fetch(`${API_URL}${editId}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, completed: false }),
      });

      setEditId(null); // edit mode ko reset krne k liye
    }

    setTitle("");
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
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Todo App</h1>

      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Enter todo"
      />

      <button onClick={handleSubmit}>
        {editId === null ? "Add" : "Update"}
      </button>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.title}

            <button onClick={() => editTodo(todo)}>Edit</button>

            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;






/* import { useEffect, useState } from "react";

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");

  const API_URL = "http://127.0.0.1:8000/api/todos/";

  // Get k liye
  const fetchTodos = async () => {
    const res = await fetch(API_URL);
    const data = await res.json();
    setTodos(data);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  // post k liye
  const addTodo = async () => {
    if (!title) return;

    await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title, completed: false }),
    });

    setTitle("");
    fetchTodos();
  };

  // delete k liye
  const deleteTodo = async (id) => {
    await fetch(`${API_URL}${id}/`, {
      method: "DELETE",
    });
    fetchTodos();
  };

  // update k liye
  const toggleComplete = async (todo) => {
    await fetch(`${API_URL}${todo.id}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: todo.title,
        completed: !todo.completed,
      }),
    });
    fetchTodos();
  };

  return (
    <div className="todoapp">
      <h1>Todos</h1>

      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Enter todo"
      />
      <button onClick={addTodo}>Add</button>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <span
              onClick={() => toggleComplete(todo)}
              style={{
                textDecoration: todo.completed ? "line-through" : "none",
                cursor: "pointer",
              }}
            >
              {todo.title}
            </span>
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
*/
