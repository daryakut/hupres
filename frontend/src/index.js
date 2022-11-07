import React from 'react';
import ReactDOM from 'react-dom';
import Home from './Home';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Quiz from "./Quiz/Quiz";
import QuizSummary from "./Quiz/QuizSummary";

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/">
            <Home/>
          </Route>
          <Route path="/quiz/:quizToken/summary" component={QuizSummary} />
          <Route path="/quiz/:quizToken" component={Quiz} />
          <Route path="/quiz">
            <Quiz/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

ReactDOM.render(<App/>, document.getElementById('root'));
