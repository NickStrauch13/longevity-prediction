import './App.css';
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import WorldMap from './pages/WorldMap';


function App() {

  return (
  <Router>
    <Navbar />
    <Routes>
      <Route exact path='/' element={<WorldMap />} />
      <Route path='/worldmap' element={<WorldMap />} />
    </Routes>
  </Router>
  )
}

export default App;