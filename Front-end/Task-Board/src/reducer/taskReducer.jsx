export default function taskReducer(state, action) {

  switch (action.type) {

    case "ADD_TASK":
      return [...state, action.payload]

    case "DELETE_TASK":
      return state.filter(task => task.id !== action.payload)

    case "UPDATE_TASK":
      return state.map(task =>
        task.id === action.payload.id ? action.payload : task
      )

    case "MOVE_TASK":
      return state.map(task =>
        task.id === action.payload.id
          ? { ...task, status: action.payload.status }
          : task
      )

    default:
      return state
  }
}