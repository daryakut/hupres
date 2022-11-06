import React, {useEffect} from 'react';
import './static/style';
import {enquireScreen} from 'enquire-js';
import {Col, Row} from "antd";
import QueueAnim from "rc-queue-anim";
import { useHistory } from 'react-router-dom';
import {createQuiz} from "../api/quizzes_api";

const Quiz = ({match}) => {
  let history = useHistory();

  const quizToken = match?.params?.quizToken;
  console.log('quizToken', quizToken)

  useEffect(() => {
    if (!quizToken) {
      async function createQuizAndLoad() {
        const quiz = (await createQuiz()).quiz;
        console.log('quiz', quiz)
        history.push(`/quiz/${quiz.token}`);
      }
      createQuizAndLoad();
    }
  }, []);

  if (!quizToken) {
    return (
      <div>Loading...</div>
    )
  }

  // const handleNavigate = () => {
  //   history.push('/some/path');
  // };

  // const {quizToken} = match.params;

  return (
    <Row justify="center" className="fullscreen-div">
      <Col span={12} offset={6}>
        <QueueAnim className="quiz-container" type="left" delay={300}>
          <div key="question">
            <h2 className="quiz-question">Форма лица</h2>
            <hr className="landing-hr"/>
          </div>
          <div key="1" className="quiz-answer">Круглое лицо</div>
          <div key="2" className="quiz-answer">Вытянутый прямоугольник</div>
          <div key="3" className="quiz-answer">Большой треугольник</div>
          <div key="4" className="quiz-answer">Малый треугольник</div>
          <div key="5" className="quiz-answer">Широк прямоугольн "Квадрат"</div>
          <div key="6" className="quiz-answer">Затрудняюсь ответить</div>
        </QueueAnim>
      </Col>
    </Row>
  );
};

export default Quiz;
