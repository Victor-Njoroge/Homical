import { useState } from 'react'
import { BrowserRouter, Routes, Route,} from 'react-router-dom';
import './App.css'
import Navbar from './components/Navbar';
import Subnavbar from './components/Subnavbar';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Navbar/>
        <Subnavbar/>
      </BrowserRouter>
    </>
  )
}

export default App
