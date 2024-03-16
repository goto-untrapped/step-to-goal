import { Route, Routes } from 'react-router-dom';
import './App.css';
import HomePage from './Components/HomePage/HomePage';

function App() {
  return (
    <div className="App">
      
      <Routes>
        <Route path="/*" element={<HomePage/>}>

        </Route>
      </Routes>

    </div>
  );
}

export default App;
