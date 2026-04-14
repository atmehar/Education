import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import Board from "./pages/Board"
import About from "./pages/About"
import { TaskProvider } from "./context/TaskContext"

export default function App() {
  return (
    <TaskProvider>
      <Router>
        <nav className="navbar">
          <h2>Task Manager</h2>

          <div>
            <Link className="nav-button" to="/">Board</Link>
            <Link className="nav-button" to="/about">About</Link>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Board />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Router>
    </TaskProvider>
  )
}