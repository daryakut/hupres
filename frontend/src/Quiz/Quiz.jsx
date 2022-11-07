import React, {useEffect, useState} from 'react';
import './static/style';
import {enquireScreen} from 'enquire-js';
import {Button, Col, Input, Row, Select} from "antd";
import QueueAnim from "rc-queue-anim";
import { useHistory } from 'react-router-dom';
import {createQuiz, getNextQuizQuestion, getQuiz, submitQuizAnswer, updateQuiz} from "../api/quizzes_api";
import Text from "antd/es/typography/Text";
import {RightOutlined} from "@ant-design/icons";

const Quiz = ({match}) => {
  let history = useHistory();
  const [quiz, setQuiz] = useState(null);
  const [question, setQuestion] = useState(null);
  const [pronounce, setPronounce] = useState(null);
  const [respondentName, setRespondentName] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const quizToken = match?.params?.quizToken;
  const quizQuestionToken = question?.quiz_question?.token

  // const quizQuestionToken = match?.params?.quizQuestionToken;
  console.log('quizToken', quizToken)
  console.log('quizQuestionToken', quizQuestionToken)
  console.log('question', question)

  useEffect(() => {
    console.log("!!!! USE EFFECT")
    if (!quizToken) {
      createQuizAndNavigate();
    } else {
      fetchQuiz().then(fetchNextQuestion);
    }
  }, [quizToken]);

  const createQuizAndNavigate = async function () {
    const quiz = (await createQuiz()).quiz;
    console.log('quiz', quiz)
    history.push(`/quiz/${quiz.token}`);
  }

  const fetchQuiz = async () => {
    try {
      // setIsLoading(true);
      const quiz = await getQuiz(quizToken);
      setQuiz(quiz);
    } catch (error) {
      // setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  const fetchNextQuestion = async () => {
    try {
      setIsLoading(true);
      const response = await getNextQuizQuestion(quizToken);
      console.log('response', response)
      setQuestion(response);
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchQuizResults = async () => {
    try {
      // setIsLoading(true);
      await updateQuiz(quizToken, respondentName, pronounce);
      // console.log('response', response)
      // setQuestion(response);
    } catch (error) {
      setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  const onGetResultsClick = async () => {
    try {
      // setIsLoading(true);
      await updateQuiz(quizToken, respondentName, pronounce);
      // console.log('response', response)
      // setQuestion(response);
    } catch (error) {
      setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  const onAnswerClick = async (answerName) => {
    await submitQuizAnswer(quizQuestionToken, answerName);
    await fetchNextQuestion();
  }

  if (error) {
    return (
      <div>Error: {error}</div>
    )
  }

  if (!quizToken || isLoading) {
    return (
      <Row justify="center" className="fullscreen-div">
        <Col span={12} offset={6}>
          Loading...
        </Col>
      </Row>
    );
  }

  if (question && !question.quiz_question) {
    if (quiz.subject_name && quiz.pronounce) {
      // Quiz already completed, let's show the results
      history.push(`/quiz/${quiz.token}/summary`);
      return null;
    }
    // End of quiz, let's ask for their name and gender
    return (
      <Row justify="center" className="fullscreen-div">
        <Col span={12} offset={6}>
          <Text className="quiz-input-label">Імʼя чи нікнейм респондента</Text>
        </Col>
        <Col span={12} offset={6}>
          <Input
            className="quiz-input"
            placeholder="Імʼя респондента"
            onChange={(e) => setRespondentName(e.target.value)}
            value={respondentName}
          />
        </Col>
        <Col span={12} offset={6}>
          <Text className="quiz-input-label">Стать чи гендер респондента</Text>
        </Col>
        <Col span={12} offset={6}>
          <Select
            placeholder="Стать респондента"
            className="quiz-input"
            onChange={setPronounce}
          >
            <Select.Option value="HE_HIM">Чоловічий</Select.Option>
            <Select.Option value="SHE_HER">Жінойчий</Select.Option>
            <Select.Option value="THEY_THEM">Інше</Select.Option>
            <Select.Option value="PREFER_NOT_TO_SAY">Не має значення</Select.Option>
          </Select>
        </Col>
        <Col span={12} offset={6}>
          <Button
            className="quiz-get-summary-button"
            size='large'
            disabled={!respondentName || !pronounce}
            onClick={onGetResultsClick}
          >
            Отримати Результат<RightOutlined />
          </Button>
        </Col>
      </Row>
    )
  }

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
        </QueueAnim>
      </Col>
    </Row>
  );
};

export default Quiz;
