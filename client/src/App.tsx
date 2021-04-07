import React from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import Home from './pages/Home';
import Engine from './pages/Engine';

const App:React.FC = () => {
  return (
    <Router>
      <Route path="/" exact component={Home} />
      <Route path="/Engine" exact component={Engine} />
    </Router>
  );
}

export default App;