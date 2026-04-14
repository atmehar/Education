import React, { useState } from "react";

function TodoApp() {
  const [title, setTitle] = useState("");

  const API_URL = "http://127.0.0.1:8000/api/todos/";


  // create k liye
  const handleSubmit = async () => {
    if (!title) return;
      await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, completed: false }),
      });

    setTitle("");
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
        Add
      </button>

    </div>
  );
}

export default TodoApp;

