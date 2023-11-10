import { AiFillGithub } from "react-icons/ai";
import { NavLink } from "react-router-dom";


const Navbar = () => {


    return (
        <nav className="navbar">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/worldmap">World Map</NavLink>
            <a href="https://github.com/NickStrauch13/longevity-prediction"><AiFillGithub size="35px" className="navbar-github"/></a>
        </nav>
    )
}

export default Navbar