import React from 'react'
import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <div className='header'>
        <div className="logo">
            <i class="fa-solid fa-house"></i>
            <span>Homical</span>
        </div>

        <div className="navigation">
            <Link>Categories</Link>
            <Link>Become a Host</Link>
            <Link>Terms</Link>
            <Link>FAQs</Link>
        </div>
        <div className="icons">
            <i class="fa-solid fa-gear"></i>
            <i class="fa-regular fa-bell"></i>
        </div>
    </div>
  )
}

export default Navbar