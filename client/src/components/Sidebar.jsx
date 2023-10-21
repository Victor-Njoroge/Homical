import React from 'react'

function Sidebar() {
    const icons=["fa-solid fa-house","fa-regular fa-calendar-days","fa-solid fa-wallet","fa-regular fa-heart","fa-regular fa-message"]
  return (
    <div className='sidebar'>
       <div className="icons">
            {icons.map((icon,index)=>(
                <i className={icon} key={index}></i>
            ))}
       </div>
       <div className="icons2">
            <i class="fa-solid fa-receipt"></i>
            <i class="fa-solid fa-power-off"></i>
       </div>
    </div>
  )
}

export default Sidebar