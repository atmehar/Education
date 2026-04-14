# Line-by-line explanations (Task-Board)

This document explains what **each line** in these folders does:

- `src/components/`
- `src/context/`
- `src/hooks/`
- `src/pages/`
- `src/reducer/`

---

## `src/components/TaskCard.jsx`

- **L1**: Imports React’s `useContext` hook so this component can read values from a Context.
- **L2**: Imports `TaskContext`, which holds `tasks`/`dispatch` for your app state.
- **L3**: Imports `Draggable` from the drag-and-drop library so a task card can be dragged.
- **L4**: Blank line for readability.
- **L5**: Exports the `TaskCard` component; it receives a `task` object and its `index` in the list.
- **L6**: Blank line for readability.
- **L7**: Reads `dispatch` from `TaskContext` so this component can send actions (delete/move).
- **L8**: Blank line for readability.
- **L9**: Starts returning JSX (the UI).
- **L10**: Wraps the card in `Draggable`; `draggableId` uniquely identifies this draggable item and `index` tells its order.
- **L11**: Blank line for readability.
- **L12**: `Draggable` uses a render-prop: it calls this function and gives you `provided` (drag props/refs).
- **L13**: Blank line for readability.
- **L14**: Starts the main wrapper `<div>` for the draggable content.
- **L15**: Blank line (there’s whitespace in JSX; not doing anything functional).
- **L16**: Attaches `provided.innerRef` so the library can control the DOM element during dragging.
- **L17**: Spreads `draggableProps` onto the element (required wiring for dragging).
- **L18**: Spreads `dragHandleProps` so the element can act as the drag “handle”.
- **L19**: Closes the opening `<div ...>` tag.
- **L20**: Opens an inner `<div>` with class `task` for styling the card.
- **L21**: Blank line for readability.
- **L22**: Renders the task title inside an `<h4>`.
- **L23**: Blank line for readability.
- **L24**: Renders the task description inside a `<p>`.
- **L25**: Blank line for readability.
- **L26**: Renders the due date in a `<small>` and inserts a `<br />` line break.
- **L27**: Opens a container `<div>` for the buttons (styled by `column-btns`).
- **L28**: Blank line for readability.
- **L29**: Starts a “Delete” `<button>`.
- **L30**: Adds `btns` class for styling.
- **L31**: Starts the click handler; it will call `dispatch(...)`.
- **L32**: Dispatches `DELETE_TASK` with the task id as payload, telling the reducer to remove it.
- **L33**: Button label text: “Delete”.
- **L34**: Closes the “Delete” button.
- **L35**: If the task is in `"todo"`, render extra buttons to move it to other columns.
- **L36**: Opens a React fragment (`<>...</>`) to return multiple sibling buttons.
- **L37**: Starts an “In Progress” button.
- **L38**: Adds `btns` class for styling.
- **L39**: Starts click handler; will dispatch an action.
- **L40**: Dispatch call begins: you’re sending an action object to the reducer.
- **L41**: Action is `MOVE_TASK`; payload sets id and new status `"progress"`.
- **L42**: Closes the dispatch call and handler.
- **L43**: Button label text: “In Progress”.
- **L44**: Closes the “In Progress” button.
- **L45**: Starts a “Completed” button (for moving directly from todo → done).
- **L46**: Adds `btns` class for styling.
- **L47**: Starts click handler; will dispatch an action.
- **L48**: Dispatches `MOVE_TASK` to set this task’s status to `"done"`.
- **L49**: Button label text: “Completed”.
- **L50**: Closes the “Completed” button.
- **L51**: Closes the fragment and the `task.status === "todo"` conditional block.
- **L52**: If the task is in `"progress"`, render a single “Completed” button.
- **L53**: Starts the button and its click handler.
- **L54**: Begins dispatch call for moving the task.
- **L55**: Dispatches `MOVE_TASK` to change status to `"done"`.
- **L56**: Closes the dispatch call/handler.
- **L57**: Button label text: “Completed”.
- **L58**: Closes the button.
- **L59**: Closes the `task.status === "progress"` conditional block.
- **L60**: If the task is already `"done"`, render a disabled “Completed” button.
- **L61**: Starts a disabled button (user can’t click it).
- **L62**: Button label text: “Completed”.
- **L63**: Closes the button.
- **L64**: Closes the `task.status === "done"` conditional block.
- **L65**: Closes the buttons container (`column-btns`).
- **L66**: Blank line for readability.
- **L67**: Closes the inner `task` div.
- **L68**: Closes the outer draggable wrapper div.
- **L69**: Blank line for readability.
- **L70**: Closes the render-prop function call.
- **L71**: Blank line for readability.
- **L72**: Closes the `Draggable` component.
- **L73**: Closes the component’s `return (...)`.
- **L74**: Closes the `TaskCard` function.

---

## `src/components/SearchBar.jsx`

- **L1**: Exports `SearchBar`; it receives the current `search` string and a `setSearch` function to update it.
- **L2**: Blank line for readability.
- **L3**: Returns JSX UI.
- **L4**: Wraps the search UI in a `search-container` div for layout/styling.
- **L5**: Starts an `<input>` element (text box).
- **L6**: Applies the `search` CSS class for styling.
- **L7**: Sets input type to `"text"` (regular text field).
- **L8**: Shows placeholder text when empty.
- **L9**: Binds the input value to `search` (controlled component).
- **L10**: On each change, updates state with the new text (`e.target.value`).
- **L11**: Closes the `<input />`.
- **L12**: Creates a container for the scrolling/marquee message.
- **L13**: Inner wrapper `design` likely used for marquee animation styling.
- **L14**: The message text shown in the marquee.
- **L15**: Closes the `design` div.
- **L16**: Closes the `marquee` div.
- **L17**: Closes the `search-container` div.
- **L18**: Closes the component’s return.
- **L19**: Closes the `SearchBar` function.
- **L20**: Trailing blank line (no functional effect).

---

## `src/components/TaskForm.jsx`

- **L1**: Imports React hooks: `useState` (form fields), `useContext` (dispatch), `useRef` (focus).
- **L2**: Imports `TaskContext` so the form can dispatch actions.
- **L3**: Blank line for readability.
- **L4**: Exports `TaskForm` component.
- **L5**: Blank line for readability.
- **L6**: Reads `dispatch` from context to add tasks.
- **L7**: Blank line for readability.
- **L8**: Creates state for `title` input and its setter.
- **L9**: Creates state for `description` input and its setter.
- **L10**: Creates state for `due` input and its setter (date).
- **L11**: Blank line for readability.
- **L12**: Creates `inputRef` to directly access the title input DOM element (to focus it later).
- **L13**: Blank line for readability.
- **L14**: Defines `submit` handler for the form submit event.
- **L15**: Prevents the browser’s default form submission (page refresh).
- **L16**: Blank line for readability.
- **L17**: If there’s no title, stop early (don’t add an empty task).
- **L18**: Blank line for readability.
- **L19**: Dispatches an action to the reducer.
- **L20**: Sets action type to `ADD_TASK`.
- **L21**: Starts the payload object (the new task).
- **L22**: Generates a unique-ish string id using current timestamp.
- **L23**: Adds the current `title` field value.
- **L24**: Adds the current `description` field value.
- **L25**: Adds the current `due` field value.
- **L26**: Sets initial status to `"todo"` so it starts in the To Do column.
- **L27**: Closes the payload object.
- **L28**: Closes the dispatched action object.
- **L29**: Blank line for readability.
- **L30**: Clears the title input after adding.
- **L31**: Clears the description input after adding.
- **L32**: Clears the due date input after adding.
- **L33**: Blank line for readability.
- **L34**: Focuses the title input again so you can quickly add another task.
- **L35**: Closes the `submit` function.
- **L36**: Blank line for readability.
- **L37**: Returns the form UI.
- **L38**: Wraps the form in a `form` div for styling/layout.
- **L39**: Displays the form heading.
- **L40**: Renders `<form>` and attaches `onSubmit={submit}` so pressing Enter triggers add.
- **L41**: Blank line for readability.
- **L42**: Title input begins.
- **L43**: Adds `input` class for styling.
- **L44**: Connects this input to `inputRef` so it can be focused programmatically.
- **L45**: Binds value to `title` state (controlled input).
- **L46**: Updates `title` on typing.
- **L47**: Placeholder for the title field.
- **L48**: Closes title input.
- **L49**: Blank line for readability.
- **L50**: Description input begins.
- **L51**: Adds `input` class for styling.
- **L52**: Binds value to `description` state.
- **L53**: Updates `description` on typing.
- **L54**: Placeholder for description.
- **L55**: Closes description input.
- **L56**: Blank line for readability.
- **L57**: Due date input begins.
- **L58**: Adds `input` class for styling.
- **L59**: Sets input type to `"date"` (browser date picker).
- **L60**: Binds value to `due` state.
- **L61**: Updates `due` on selecting a date.
- **L62**: Closes due date input.
- **L63**: Blank line for readability.
- **L64**: Submit button to add the task.
- **L65**: Blank line for readability.
- **L66**: Closes the `<form>`.
- **L67**: Closes the wrapper div.
- **L68**: Closes the return.
- **L69**: Closes the `TaskForm` function.

---

## `src/components/Column.jsx`

- **L1**: Imports `Droppable` so this column can accept dragged items.
- **L2**: Imports `TaskCard` for rendering each task item.
- **L3**: Blank line for readability.
- **L4**: Exports `Column`; receives a `status` key, a visible `title`, and the full `tasks` list.
- **L5**: Blank line for readability.
- **L6**: Filters tasks to only those matching this column’s `status`.
- **L7**: Blank line for readability.
- **L8**: Returns JSX UI.
- **L9**: Wraps the column in `Droppable`; `droppableId` identifies this drop target (here it equals the status).
- **L10**: Render-prop function gets `provided` which contains the droppable wiring.
- **L11**: Starts the column container div.
- **L12**: Applies `column` class for styling.
- **L13**: Attaches `provided.innerRef` so the library can measure/manage this droppable area.
- **L14**: Spreads `droppableProps` onto the element (required droppable wiring).
- **L15**: Closes the opening div tag.
- **L16**: Renders the column title (e.g., “To Do”).
- **L17**: Blank line for readability.
- **L18**: Maps each filtered task to a `TaskCard` and provides its `index` for drag ordering.
- **L19**: Renders `TaskCard` with a stable `key`, plus `task` and `index` props.
- **L20**: Closes the map.
- **L21**: Blank line for readability.
- **L22**: Renders `provided.placeholder`, which reserves space while dragging (prevents layout jump).
- **L23**: Blank line for readability.
- **L24**: Closes the column container div.
- **L25**: Closes the render-prop function.
- **L26**: Closes the `Droppable`.
- **L27**: Closes the return.
- **L28**: Closes the `Column` function.

---

## `src/context/TaskContext.jsx`

- **L1**: Imports `createContext` (to create context), `useReducer` (state management), `useEffect` (side effects).
- **L2**: Imports the reducer function that handles actions on tasks.
- **L3**: Blank line for readability.
- **L4**: Creates and exports `TaskContext` (initial value is undefined until Provider sets it).
- **L5**: Blank line for readability.
- **L6**: Exports `TaskProvider`, a component that wraps your app and provides tasks/dispatch to children.
- **L7**: Blank line for readability.
- **L8**: Reads previously saved tasks from `localStorage` under the key `"tasks"`.
- **L9**: Parses stored JSON if present; otherwise uses an empty list as initial tasks.
- **L10**: Blank line for readability.
- **L11**: Creates reducer state: `tasks` is current state, `dispatch` sends actions to `taskReducer`.
- **L12**: Blank line for readability.
- **L13**: Runs a side effect whenever `tasks` changes.
- **L14**: Saves the latest tasks array to `localStorage` as JSON (persistence across refresh).
- **L15**: Dependency array `[tasks]` means this effect runs after any task change.
- **L16**: Blank line for readability.
- **L17**: Returns the Provider component that supplies values to the component tree.
- **L18**: Sets the context value to an object containing `tasks` and `dispatch`.
- **L19**: Renders whatever components are wrapped by `TaskProvider`.
- **L20**: Closes the Provider.
- **L21**: Closes the return.
- **L22**: Closes the `TaskProvider` function.

---

## `src/hooks/useLocalStorage.jsx`

- **L1**: Imports hooks: `useEffect` (sync to storage) and `useState` (hold value).
- **L2**: Blank line for readability.
- **L3**: Exports a custom hook that stores state in `localStorage` using `key`, defaulting to `initialValue`.
- **L4**: Blank line for readability.
- **L5**: Initializes state with a function (lazy init) so storage is read only once on mount.
- **L6**: Reads a value from localStorage for this key.
- **L7**: If found, parse JSON; else use the provided `initialValue`.
- **L8**: Closes the lazy initializer and state call.
- **L9**: Blank line for readability.
- **L10**: Side effect runs when `key` or `value` changes.
- **L11**: Saves the latest `value` to localStorage as JSON.
- **L12**: Dependency array ensures syncing happens on relevant changes.
- **L13**: Blank line for readability.
- **L14**: Returns the same shape as `useState`: current value and a setter.
- **L15**: Closes the hook function.

---

## `src/pages/Board.jsx`

- **L1**: Imports `useContext` (read tasks/dispatch) and `useState` (search).
- **L2**: Imports `TaskContext` to access global tasks state.
- **L3**: Imports `Column` component for each status column.
- **L4**: Imports `TaskForm` component for adding new tasks.
- **L5**: Imports `SearchBar` component for filtering tasks by title.
- **L6**: Blank line for readability.
- **L7**: Imports `DragDropContext`, the top-level wrapper required by the DnD library.
- **L8**: Blank line for readability.
- **L9**: Exports `Board` page component (main task board UI).
- **L10**: Blank line for readability.
- **L11**: Reads `tasks` and `dispatch` from context.
- **L12**: Blank line for readability.
- **L13**: Comment: indicates the next lines define search state.
- **L14**: Creates `search` state for the search query string.
- **L15**: Blank line for readability.
- **L16**: Comment: indicates the next lines define drag handler.
- **L17**: Defines `onDragEnd`, called when a drag operation finishes.
- **L18**: Blank line for readability.
- **L19**: If the item was dropped outside any droppable, stop (no changes).
- **L20**: Blank line for readability.
- **L21**: Dispatches an action to update task status after a drop.
- **L22**: Uses `MOVE_TASK` to change which column the task belongs to.
- **L23**: Starts payload object.
- **L24**: Uses `result.draggableId` (the task id) to identify which task moved.
- **L25**: Uses `result.destination.droppableId` (column id) as the new status.
- **L26**: Closes payload object.
- **L27**: Closes the action object.
- **L28**: Closes `onDragEnd` function.
- **L29**: Blank line for readability.
- **L30**: Comment: indicates the next lines filter tasks by the search term.
- **L31**: Filters tasks array; keeps tasks whose title matches the search query.
- **L32**: Converts both title and search to lowercase so matching is case-insensitive.
- **L33**: Closes the filter call.
- **L34**: Blank line for readability.
- **L35**: Returns the board UI.
- **L36**: Outer wrapper div.
- **L37**: Blank line for readability.
- **L38**: Renders the add-task form above the board.
- **L39**: Blank line for readability.
- **L40**: JSX comment for the search bar section.
- **L41**: Renders `SearchBar` with current search and its setter.
- **L42**: Blank line for readability.
- **L43**: Wraps columns in `DragDropContext` and supplies the `onDragEnd` handler.
- **L44**: Blank line for readability.
- **L45**: Board layout container (likely flex/grid via CSS).
- **L46**: Blank line for readability.
- **L47**: Renders To Do column; passes filtered tasks so search applies.
- **L48**: Renders In Progress column.
- **L49**: Renders Done column.
- **L50**: Blank line for readability.
- **L51**: Closes the board container div.
- **L52**: Blank line for readability.
- **L53**: Closes `DragDropContext`.
- **L54**: Blank line for readability.
- **L55**: Closes the outer wrapper div.
- **L56**: Closes the return.
- **L57**: Closes the `Board` function.

---

## `src/pages/About.jsx`

- **L1**: Exports the `About` page component.
- **L2**: Returns JSX UI.
- **L3**: Wrapper div with class `page` for styling.
- **L4**: Heading text.
- **L5**: Paragraph describing the project.
- **L6**: Closes the wrapper div.
- **L7**: Closes the return.
- **L8**: Closes the `About` function.

---

## `src/reducer/taskReducer.jsx`

- **L1**: Exports `taskReducer`, a pure function that returns the next state based on current `state` and an `action`.
- **L2**: Blank line for readability.
- **L3**: Starts a `switch` on `action.type` to decide how to update state.
- **L4**: Blank line for readability.
- **L5**: Case: handle adding a task.
- **L6**: Returns a new array containing all existing tasks plus the new task payload (immutably).
- **L7**: Blank line for readability.
- **L8**: Case: handle deleting a task.
- **L9**: Returns a new array excluding the task whose id equals the payload.
- **L10**: Blank line for readability.
- **L11**: Case: handle updating a task (replace the task object).
- **L12**: Maps over tasks to build a new array.
- **L13**: If ids match, replace with the payload; otherwise keep the original task.
- **L14**: Closes the map callback.
- **L15**: Blank line for readability.
- **L16**: Case: handle moving a task between columns.
- **L17**: Maps over tasks to build a new array.
- **L18**: Checks if this is the task being moved.
- **L19**: If yes, returns a copy of the task with updated `status`.
- **L20**: Otherwise returns the task unchanged.
- **L21**: Closes the map callback.
- **L22**: Blank line for readability.
- **L23**: Default: if action type is unknown, don’t change state.
- **L24**: Returns the current state unchanged.
- **L25**: Closes the switch.
- **L26**: Closes the reducer function.

