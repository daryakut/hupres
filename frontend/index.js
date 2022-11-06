import React from 'react';
import ReactDOM from 'react-dom';
import Home from './src/Home';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Quiz from "./src/Quiz";

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/">
            <Home/>
          </Route>
          <Route path="/quiz">
            <Quiz/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

ReactDOM.render(<App/>, document.getElementById('root'));
