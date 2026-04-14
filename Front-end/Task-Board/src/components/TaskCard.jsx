import { useContext } from "react"
import { TaskContext } from "../context/TaskContext"
import { Draggable } from "@hello-pangea/dnd"

export default function TaskCard({ task, index }) {

    const { dispatch } = useContext(TaskContext)

    return (
        <Draggable draggableId={task.id} index={index}>

            {(provided) => (

                <div
                    
                    ref={provided.innerRef}
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                >
                    <div className="task">

                    <h4>{task.title}</h4>

                    <p>{task.description}</p>

                    <small>{task.due}</small><br />
                    <div className="column-btns">

                    <button
                    className="btns"
                        onClick={() =>
                            dispatch({ type: "DELETE_TASK", payload: task.id })}>
                        Delete
                    </button>
                    {task.status === "todo" && (
                        <>
                            <button
                            className="btns"
                                onClick={() =>
                                    dispatch({
                                        type: "MOVE_TASK", payload: { id: task.id, status: "progress" },
                                    })}>
                                In Progress
                            </button>
                            <button
                            className="btns"
                                onClick={() =>
                                    dispatch({ type: "MOVE_TASK", payload: { id: task.id, status: "done" }, })}>
                                Completed
                            </button>
                        </>)}
                    {task.status === "progress" && (
                        <button onClick={() =>
                            dispatch({
                                type: "MOVE_TASK", payload: { id: task.id, status: "done" },
                            })}>
                            Completed
                        </button>
                    )}
                    {task.status === "done" && (
                        <button disabled>
                            Completed
                        </button>
                    )}
                    </div>

                </div>
                </div>

            )}

        </Draggable>
    )
}