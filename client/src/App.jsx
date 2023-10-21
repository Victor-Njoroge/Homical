import { useState } from 'react'
import { BrowserRouter, Routes, Route,} from 'react-router-dom';
import './App.css'
import Navbar from './components/Navbar';
import Subnavbar from './components/Subnavbar';
import Sidebar from './components/Sidebar';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Navbar/>
        <Subnavbar/>
        <Sidebar/>
      </BrowserRouter>
    </>
  )
}

export default App
