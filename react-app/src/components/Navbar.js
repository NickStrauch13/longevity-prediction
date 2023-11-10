import { AiFillGithub } from "react-icons/ai";
import { NavLink } from "react-router-dom";


const Navbar = () => {


    return (
        <nav className="navbar">
            <div className="navbar-link-container">
                <NavLink to="/" className="navbar-link-text">Home</NavLink>
            </div>
            <div className="navbar-link-container">
                <NavLink to="/worldmap" className="navbar-link-text">World Map</NavLink>
            </div>
            <a href="https://github.com/NickStrauch13/longevity-prediction"><AiFillGithub size="35px" className="navbar-github"/></a>
        </nav>
    )
}

export default Navbar