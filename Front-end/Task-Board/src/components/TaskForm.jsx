import { useState, useContext, useRef } from "react"
import { TaskContext } from "../context/TaskContext"

export default function TaskForm() {

    const { dispatch } = useContext(TaskContext)

    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")
    const [due, setDue] = useState("")

    const inputRef = useRef()

    const submit = (e) => {
        e.preventDefault()

        if (!title) return

        dispatch({
            type: "ADD_TASK",
            payload: {
                id: Date.now().toString(),
                title,
                description,
                due,
                status: "todo"
            }
        })

        setTitle("")
        setDescription("")
        setDue("")

        inputRef.current.focus()
    }

    return (
        <div className="form">
            <h1>Add a Task</h1>
            <form className="task-form" onSubmit={submit}>

                <input
                    className="input"
                    ref={inputRef}
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Task Title"
                />

                <input
                    className="input"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Description"
                />

                <input
                    className="input"
                    type="date"
                    value={due}
                    onChange={(e) => setDue(e.target.value)}
                />

                <button className="button">Add Task</button>

            </form>
        </div>
    )
}