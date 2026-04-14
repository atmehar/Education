import { useContext, useState } from "react"
import { TaskContext } from "../context/TaskContext"
import Column from "../components/Column"
import TaskForm from "../components/TaskForm"
import SearchBar from "../components/SearchBar"

import { DragDropContext } from "@hello-pangea/dnd"

export default function Board() {

    const { tasks, dispatch } = useContext(TaskContext)

    // search state
    const [search, setSearch] = useState("")

    // drag function
    const onDragEnd = (result) => {

        if (!result.destination) return

        dispatch({
            type: "MOVE_TASK",
            payload: {
                id: result.draggableId,
                status: result.destination.droppableId
            }
        })
    }

    // filter tasks for search
    const filteredTasks = tasks.filter((task) =>
        task.title.toLowerCase().includes(search.toLowerCase())
    )

    return (
        <div>

            <TaskForm />

            {/* search bar */}
            <SearchBar search={search} setSearch={setSearch} />

            <DragDropContext onDragEnd={onDragEnd}>

                <div className="board">

                    <Column status="todo" title="To Do" tasks={filteredTasks} />
                    <Column status="progress" title="In Progress" tasks={filteredTasks} />
                    <Column status="done" title="Done" tasks={filteredTasks} />

                </div>

            </DragDropContext>

        </div>
    )
}