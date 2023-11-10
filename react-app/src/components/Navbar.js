import React, { useState } from "react";
import { AiOutlineBars, AiFillGithub } from "react-icons/ai";
import { NavLink } from "react-router-dom";


const Navbar = () => {

    const [toggleDropdown, setToggleDropdown] = useState(false);

    function handleMenuClick() {
        setToggleDropdown(prevDropdownState => !prevDropdownState)
    }


    return (
        <nav className="navbar">
            <AiOutlineBars size="35px" onClick={() => handleMenuClick()} style={{ cursor: 'pointer' }} className="navbar-menu"/>  
            <h1 className="navbar-title">Longevity Prediction</h1>
            <a href="https://github.com/NickStrauch13/longevity-prediction"><AiFillGithub size="35px" className="navbar-github"/></a>
            <NavLink to="/">Home</NavLink>
        </nav>
    )
}

export default Navbar