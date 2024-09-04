import React from 'react';
import './App.css';
import MyApp from './components/MyApp';
import logo from './logo.svg';

function App() {
  return (
    <div className="App">
      <MyApp />
        <div className="card w-96 bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">DaisyUI Card</h2>
            <p>This is a test card using DaisyUI styles.</p>
          </div>
        </div>

      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
