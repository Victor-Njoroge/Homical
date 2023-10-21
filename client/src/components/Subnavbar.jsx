import React from 'react'

function Subnavbar() {
    const variety=['Flat', 'Luxury', 'Camping', 'A-Frame', 'Lake Villa']
  return (
    <div className='sub header'>
        <div className="searchbox">
            <input type="text" placeholder='Search in Homes, Villas, Appartments ...' />
            <i class="fa-solid fa-magnifying-glass"></i>
        </div>
        <div className="recomendation">
            <span>Recommended: </span>
            {variety.map((variety,index)=>(
                <button key={index}>{variety}</button>
            ))}
        </div>
    </div>
  )
}

export default Subnavbar