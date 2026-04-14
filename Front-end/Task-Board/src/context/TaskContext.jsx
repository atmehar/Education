import { createContext, useReducer, useEffect } from "react"
import taskReducer from "../reducer/taskReducer"

export const TaskContext = createContext()

export function TaskProvider({ children }) {

  const stored = localStorage.getItem("tasks")
  const initialState = stored ? JSON.parse(stored) : []

  const [tasks, dispatch] = useReducer(taskReducer, initialState)

  useEffect(() => {
    localStorage.setItem("tasks", JSON.stringify(tasks))
  }, [tasks])

  return (
    <TaskContext.Provider value={{ tasks, dispatch }}>
      {children}
    </TaskContext.Provider>
  )
}