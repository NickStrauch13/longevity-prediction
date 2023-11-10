import './App.css';
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';


function App() {

  return (
    <Router>
            <Navbar />
            <Routes>
                <Route exact path='/' element={<Home />} />
            </Routes>
        </Router>
  )
}

export default App;