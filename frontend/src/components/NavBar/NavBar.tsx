
import React from "react"
import {Link} from "react-router-dom";
import cl from './NavBar.module.css'

const NavBar: React.FC = () => {
    return (
        <div className={cl.navbar}>
            <div className={cl.navBar__links}>
                <Link to="/images" className={cl.link}>Images</Link>
        </div>
            <div className={cl.navBar__links}>
                <Link to="/tasks" className={cl.link}>Tasks</Link>
            </div>
        </div>
    )
}

export default NavBar;