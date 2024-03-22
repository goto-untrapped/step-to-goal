import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // レンダリングするReactコンポーネント

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root') // index.html 内の要素にレンダリング
);
