import { Link } from "react-router-dom"

const Home = () => {
    return (
        <div className="home">
            <div className="Home-card">
                <h1>Welcome</h1>
                <div className="div-btn">
                    <Link to = "/todos"><button>View Todos</button></Link>
                    <Link to = "/add-todos"><button>Add Todos</button></Link>
                </div>
            </div>
        </div>
    )
}

export default Home