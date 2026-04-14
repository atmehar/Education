import { Droppable } from "@hello-pangea/dnd"
import TaskCard from "./TaskCard"

export default function Column({ status, title, tasks }) {

  const filtered = tasks.filter(task => task.status === status)

  return (
    <Droppable droppableId={status}>
      {(provided) => (
        <div
          className="column"
          ref={provided.innerRef}
          {...provided.droppableProps}
        >
          <h3>{title}</h3>

          {filtered.map((task, index) => (
            <TaskCard key={task.id} task={task} index={index} />
          ))}

          {provided.placeholder}

        </div>
      )}
    </Droppable>
  )
}