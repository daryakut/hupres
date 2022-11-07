import React, {useEffect, useState} from 'react';
import './static/style';
import {enquireScreen} from 'enquire-js';
import {Col, Row} from "antd";
import QueueAnim from "rc-queue-anim";
import { useHistory } from 'react-router-dom';
import {createQuiz, getNextQuizQuestion, submitQuizAnswer} from "../api/quizzes_api";

const Quiz = ({match}) => {
  let history = useHistory();
  const [question, setQuestion] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const quizQuestionToken = question?.question?.quiz_question?.token

  const quizToken = match?.params?.quizToken;
  // const quizQuestionToken = match?.params?.quizQuestionToken;
  console.log('quizToken', quizToken)
  console.log('quizQuestionToken', quizQuestionToken)
  console.log('question', question)

  const fetchNextQuestion = async () => {
    try {
      setIsLoading(true);
      const response = (await getNextQuizQuestion(quizToken)).quiz;
      console.log('response', response)
      setQuestion(response);
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  const onAnswerClick = async (answerName) => {
    await submitQuizAnswer(quizQuestionToken, answerName);
    await fetchNextQuestion();
    // history.push('/some/path');
  }

  useEffect(() => {
    if (!quizToken) {
      async function createQuizAndLoad() {
        const quiz = (await createQuiz()).quiz;
        console.log('quiz', quiz)
        history.push(`/quiz/${quiz.token}`);
      }
      createQuizAndLoad();
    } else {
      fetchNextQuestion();
    }
  }, []);

  if (!quizToken || isLoading) {
    return (
      <div>Loading...</div>
    )
  }

  if (error) {
    return (
      <div>Error: {error}</div>
    )
  }

  // const handleNavigate = () => {
  //   history.push('/some/path');
  // };

  // const {quizToken} = match.params;

  const displayQuestion = question?.quiz_question?.question_display_name;
  const displayAnswers = question?.available_answers;

  return (
    <Row justify="center" className="fullscreen-div">
      <Col span={12} offset={6}>
        <QueueAnim className="quiz-container" type="left" delay={300}>
          <div key="question">
            <h2 className="quiz-question">{displayQuestion}</h2>
            <hr className="landing-hr"/>
          </div>
          {
            displayAnswers.map((answer, index) => (
              <div key={`answer-${index}`} className="quiz-answer" onClick={() => onAnswerClick(answer.answer_name)}>
                {answer.answer_display_name}
              </div>
            ))
          }
          {/*<div key="1" className="quiz-answer">Круглое лицо</div>*/}
          {/*<div key="2" className="quiz-answer">Вытянутый прямоугольник</div>*/}
          {/*<div key="3" className="quiz-answer">Большой треугольник</div>*/}
          {/*<div key="4" className="quiz-answer">Малый треугольник</div>*/}
          {/*<div key="5" className="quiz-answer">Широк прямоугольн "Квадрат"</div>*/}
          {/*<div key="6" className="quiz-answer">Затрудняюсь ответить</div>*/}
        </QueueAnim>
      </Col>
    </Row>
  );
};

export default Quiz;
