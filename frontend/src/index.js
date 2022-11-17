import React from 'react';
import ReactDOM from 'react-dom';
import Home from './Home';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Quiz from "./Quiz/Quiz";
import QuizSummary from "./Quiz/QuizSummary";
import {UserProvider} from "./User/UserProvider";
import Quizzes from "./Quiz/Quizzes";
import { createRoot } from 'react-dom/client';
import Disclaimer from "./Home/Disclaimer";

const App = () => {
  return (
    <Router>
      <UserProvider>
        <div>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/quiz/:quizToken/summary" component={QuizSummary}/>
            <Route path="/quiz/:quizToken" component={Quiz}/>
            <Route path="/quiz"><Quiz/></Route>
            <Route path="/quizzes"><Quizzes/></Route>
            <Route path="/disclaimer"><Disclaimer/></Route>
          </Switch>
        </div>
      </UserProvider>
    </Router>
  );
};

// ReactDOM.render(<App/>, document.getElementById('root'));
// Assuming your HTML has a div with id 'root'
const container = document.getElementById('root');
const root = createRoot(container); // create a root
root.render(<App />); // use the render method on the root
