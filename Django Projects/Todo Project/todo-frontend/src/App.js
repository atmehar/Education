import Home from "./Pages/Home";
import "./index.css";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ViewTodo from "./Pages/ViewTodo"
import AddTodo from "./Pages/AddTodo"

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/todos" element={<ViewTodo/>} />
            <Route path="/add-todos" element={<AddTodo/>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;