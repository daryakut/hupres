import React, {useEffect, useState} from 'react';
import './static/style';
import {enquireScreen} from 'enquire-js';
import {Button, Card, Checkbox, Col, Input, Row, Select} from "antd";
import QueueAnim from "rc-queue-anim";
import {useHistory} from 'react-router-dom';
import {createQuiz, getNextQuizQuestion, getQuiz, submitQuizAnswer, updateQuiz} from "../api/quizzes_api";
import Text from "antd/es/typography/Text";
import {RightOutlined} from "@ant-design/icons";
import Header from "../Home/Header";

const Quiz = ({match}) => {
  let history = useHistory();
  const [quiz, setQuiz] = useState(null);
  const [question, setQuestion] = useState(null);
  const [answers, setAnswers] = useState([]);
  const [isQuizComplete, setQuizComplete] = useState(false);
  const [pronounce, setPronounce] = useState(null);
  const [respondentName, setRespondentName] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const quizToken = match?.params?.quizToken;
  const quizQuestionToken = question?.token

  // const quizQuestionToken = match?.params?.quizQuestionToken;
  console.log('quizToken', quizToken)
  console.log('quizQuestionToken', quizQuestionToken)
  console.log('question', question)

  const marginTop = Math.max(10, 360 - answers.length * 16);

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
    history.replace(`/quiz/${quiz.token}`);
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
      setQuestion(response.quiz_question);
      setAnswers(response.available_answers);
      // Quiz is complete if there is no question
      setQuizComplete(!response.quiz_question);
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  const onGetResultsClick = async () => {
    try {
      // setIsLoading(true);
      await updateQuiz(quizToken, respondentName, pronounce);
      // console.log('response', response)
      // setQuestion(response);
      history.replace(`/quiz/${quiz.token}/summary`);
    } catch (error) {
      setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  const onAnswerClick = async (answerName) => {
    // const answerIndex = answers.findIndex(answer => answer.answer_name === answerName);
    // const answersCopy = answers.slice(0);
    // answersCopy.splice(answerIndex, 1)
    // setAnswers([]);

    await submitQuizAnswer(quizQuestionToken, answerName);
    await fetchNextQuestion();
  }

  if (error) {
    return (
      <div>Error: {error}</div>
    )
  }

  if (!quizToken || isLoading) {
    // This looks makes the impression of new quiz paper being added
    return (
      <Row justify="center" className="fullscreen-div">
      </Row>
    );
  }

  if (isQuizComplete) {
    if (quiz.subject_name && quiz.pronounce) {
      // Quiz already completed, let's show the results
      history.replace(`/quiz/${quiz.token}/summary`);
      return null;
    }

    // End of quiz, let's ask for their name and gender
    return (
      <>
        <Header/>
        <div className="fullscreen-div">
          <Row justify="center">
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>
              <div className="quiz-container quiz-container-summary" style={{ marginTop: 300 }}>
                <div className="quiz-input-container">
                  <Text className="quiz-input-label quiz-font">Імʼя чи нікнейм респондента</Text>
                  <Input
                    className="quiz-input quiz-font"
                    placeholder="Імʼя респондента"
                    onChange={(e) => setRespondentName(e.target.value)}
                    value={respondentName}
                  />
                  <Text className="quiz-input-label quiz-font">Стать чи гендер респондента</Text>
                  <Select
                    placeholder="Стать респондента"
                    className="quiz-input quiz-font"
                    onChange={setPronounce}
                  >
                    <Select.Option value="HE_HIM">Чоловічий</Select.Option>
                    <Select.Option value="SHE_HER">Жінойчий</Select.Option>
                    <Select.Option value="THEY_THEM">Інше</Select.Option>
                    <Select.Option value="PREFER_NOT_TO_SAY">Не має значення</Select.Option>
                  </Select>
                  <Button
                    className="quiz-get-summary-button quiz-font-large"
                    size='large'
                    disabled={!respondentName || !pronounce}
                    onClick={onGetResultsClick}
                  >
                    Отримати Результат<RightOutlined/>
                  </Button>
                </div>
              </div>
            </Col>
          </Row>
        </div>
      </>
    )
  }

  const displayQuestion = question?.question_display_name;

  return (
    <>
      <Header/>
      <div className="fullscreen-div">
        <Row justify="center">
          <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
          <Col xs={22} sm={20} md={16} lg={12} xl={10}>
            {/*<Card className="quiz-card" title="Card title" bordered={false}>*/}
            {/*  <p>Card content</p>*/}
            {/*  <p>Card content</p>*/}
            {/*  <p>Card content</p>*/}
            {/*</Card>*/}
            <div className="quiz-container" style={{marginTop}}>
              <QueueAnim
                type="left"
                delay={300}
                // enterAnim={[
                //   { opacity: [1, 0], translateY: [0, 50] },
                //   { height: [200, 0], duration: [500, 0] }
                // ]}
                // leaveAnim={[
                //   { opacity: [0, 1], translateY: [50, 0] },
                //   { height: 0 }
                // ]}
              >
                <div key="question">
                  <h2 className="quiz-question">{displayQuestion}</h2>
                  <hr className="quiz-hr"/>
                </div>
                {
                  answers.map((answer, index) => (
                    <Checkbox
                      key={`answer-${index}`}
                      className="quiz-answer"
                      onChange={() => onAnswerClick(answer.answer_name)}>
                      {answer.answer_display_name}
                    </Checkbox>
                    // <div key={`answer-${index}`} className="quiz-answer"
                    //      onClick={() => onAnswerClick(answer.answer_name)}>
                    //   {answer.answer_display_name}
                    // </div>
                  ))
                }
              </QueueAnim>
            </div>
          </Col>
        </Row>
      </div>
    </>
  );
};

export default Quiz;
