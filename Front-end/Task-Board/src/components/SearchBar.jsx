export default function SearchBar({ search, setSearch }) {

    return (
        <div className="search-container">
            <input
                className="search"
                type="text"
                placeholder="Search task..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />
            <div className="marquee">
                <div className="design">
                    This is a Task page.Every task has a Deadline. You need to Complete your task before the Deadline. All the best! Thank You!
                </div>
            </div>
        </div>
    )
}
