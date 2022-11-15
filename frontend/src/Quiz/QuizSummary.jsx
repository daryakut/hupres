import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Col, Modal, Row} from "antd";
import {useHistory} from 'react-router-dom';
import {askFreeFormQuestion, generateQuizSummary, getFreeFormQuestions} from "../api/quizzes_api";
import Text from "antd/es/typography/Text";
import {CopyOutlined, LoadingOutlined} from "@ant-design/icons";
import TextArea from "antd/es/input/TextArea";
import {useUser} from "../User/UserProvider";
import Header from "../Home/Header";
import {getBaseUrl} from "../api/server";
import QuizContainer from "./QuizContainer";

const QuizSummary = ({match}) => {
  let history = useHistory();
  const {user} = useUser();
  const [summaries, setSummaries] = useState([]);
  const [questions, setQuestions] = useState([]);
  const [freeFormQuestion, setFreeFormQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const [error, setError] = useState(null);

  // Only logged in users can chat with AI
  const canChatWithAi = !!user;
  // const canChatWithAi = false;

  const quizToken = match.params.quizToken;

  useEffect(() => {
    fetchQuizSummary();
  }, [quizToken]);

  const fetchQuizSummary = async () => {
    // Grab the recent form content from localStorage
    const freeFormQuestionContent = localStorage.getItem('freeFormQuestionContent');
    if (freeFormQuestionContent) {
      setFreeFormQuestion(freeFormQuestionContent)
      localStorage.removeItem('freeFormQuestionContent');
    }

    try {
      // setIsLoading(true);
      const summaries = (await generateQuizSummary(quizToken)).summaries;
      setSummaries(summaries);

      const questions = (await getFreeFormQuestions(quizToken));
      setQuestions(questions ?? []);
      // await askFreeFormQuestion(quizToken, "Как лучше всего смотивировать сотрудника?");
    } catch (error) {
      // setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  const onAskFreeFormQuestionClick = async () => {
    if (!canChatWithAi) {
      setIsLoginModalOpen(true)
      return
    }

    try {
      const originalQuestions = questions.slice(0);
      // setIsLoading(true);
      setQuestions(originalQuestions.concat({question: freeFormQuestion, answer: null}));
      setTimeout(() => {
        window.scrollTo({
          top: document.body.scrollHeight,
          behavior: 'smooth'
        });
      })

      const freeFormAnswer = (await askFreeFormQuestion(quizToken, freeFormQuestion));
      console.log('freeFormAnswer', freeFormAnswer)

      setQuestions(originalQuestions.concat({question: freeFormQuestion, answer: freeFormAnswer}));
      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
      });
    } catch (error) {
      // setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  const onCopyToClipboardClick = async () => {
    const summariesStringList = summaries.map((summary) => `${summary.title}: ${summary.summary}`)
    const chatsStringList = questions.map((question) => ` - ${question.question} \n - ${question.answer}`)
    const clipboard = summariesStringList.join('\n\n') + '\n\n---\n\n' + chatsStringList.join('\n\n---\n\n')
    await navigator.clipboard.writeText(clipboard)
  };

  const onFreeFormQuestionKeyDown = async (event) => {
    if (event.key === 'Enter' || event.keyCode === 13) {
      event.preventDefault();
      if (canChatWithAi) {
        setFreeFormQuestion('');
      }
      await onAskFreeFormQuestionClick();
    }
  }

  const onRegisterOrLoginClick = async (event) => {
    // Store the redirect URL in localStorage so that user sees the same quiz after login
    localStorage.setItem('redirectUrl', `/quiz/${quizToken}/summary`);
    // Also store the question content for convenience
    localStorage.setItem('freeFormQuestionContent', freeFormQuestion);
  }

  if (isLoading) {
    return (
      <div className="fullscreen-div">
        <div className="fullscreen-div-center">
          <LoadingOutlined className="loading-icon"/>
        </div>
      </div>
    );
  }

  if (!isLoading && !summaries.length) {
    return (
      <div className="fullscreen-div">
        <div className="fullscreen-div-center">
          <div className="quiz-container quiz-container-summary">
            <div className="free-form-answer-container">
              Анкета ще не заповнена!
            </div>
            <Button
              className="cta-button"
              size='large'
              onClick={() => history.replace(`/quiz/${quizToken}`)}
            >
              Продовжити анкетування
            </Button>
          </div>
        </div>
      </div>
    )
  }

  console.log('freeFormQuestion', freeFormQuestion)

  return (
    <>
      <Header key="header"/>
      {/*<div style={{height: 80}}/>*/}
      <div className="fullscreen-div-scrollable">
        <QuizContainer>
          <div className="quiz-container quiz-container-summary">
            <div className="copy-to-clipboard-button-container">
              <Button className="copy-to-clipboard-button" onClick={onCopyToClipboardClick}><CopyOutlined/></Button>
            </div>
            {
              summaries.map((summary, index) => (
                <Row key={`summary-${index}`} justify="center">
                  <Col span={24}>
                    <h2 className="quiz-summary-title">{summary.title}</h2>
                    <h5 className="quiz-summary-content">{summary.summary}</h5>
                  </Col>
                </Row>
              ))
            }
          </div>

          <div className="free-form-chat-container">
            {
              questions.map((question, index) => (
                <div key={`question-${index}`}>
                  <hr className="free-form-hr-divider"/>
                  <div key={`question-${index}`} className="free-form-question-container">
                    {/*<Col key={`summary-${index}`} span={16} offset={8}>*/}
                    <h5 className="free-form-question-content" style={{textAlign: 'right'}}>{question.question}</h5>
                    {/*</Col>*/}
                  </div>
                  <div key={`answer-${index}`} className="free-form-answer-container">
                    {question.answer ? (
                      <h5 className="free-form-answer-content">{question.answer}</h5>
                    ) : (
                      <div className="free-form-answer-content"><LoadingOutlined/></div>
                    )}
                  </div>
                </div>
              ))
            }
          </div>

          <div style={{height: 100}}/>
        </QuizContainer>

        <div className="free-form-question-input-container">
          <div className="free-form-question-input-container-fade"/>
          <div className="free-form-question-input-container-white">
            {/*<Row>*/}
            {/*  <Col xs={0} sm={0} md={1} lg={2} xl={3}/>*/}
            {/*  <Col xs={24} sm={24} md={20} lg={20} xl={18}>*/}
            <Row>
              <Col span={24} offset={0}>
                <Text className="free-form-question-input-label">
                  Ви також можете запитати що вас цікавить стосовно респондента у нашого AI помічника
                </Text>
              </Col>
            </Row>
            <Row style={{marginTop: 6}}>
              <Col xs={16} sm={18} md={20} lg={21} xl={21}>
                {/*<Input*/}
                <TextArea rows={2}
                          className="free-form-question-input"
                          placeholder="Як мотивуваті цього респондента?"
                          value={freeFormQuestion}
                          onChange={(e) => setFreeFormQuestion(e.target.value)}
                          onKeyDown={onFreeFormQuestionKeyDown}
                />
              </Col>
              <Col xs={8} sm={6} md={4} lg={3} xl={3}>
                <Button
                  className="free-form-question-button"
                  size='large'
                  disabled={!freeFormQuestion}
                  onClick={onAskFreeFormQuestionClick}
                >
                  Спитати
                </Button>
              </Col>
            </Row>
            {/*  </Col>*/}
            {/*</Row>*/}
          </div>
        </div>
      </div>
      <Modal
        title="Щоб продовжити, зареєструйтесь!"
        visible={isLoginModalOpen}
        onCancel={() => setIsLoginModalOpen(false)}
        footer={[]}
        centered
      >
        <div className="quiz-summary-login-modal">
          <a href={`${getBaseUrl()}/api/users/google-login`}
             className="quiz-summary-login-link"
             onClick={onRegisterOrLoginClick}
          >
            <Button
              size='large'
              className="quiz-summary-login-button cta-button"
            >
              РЕЄСТРАЦІЯ
            </Button>
          </a>
          <a href={`${getBaseUrl()}/api/users/google-login`}
             className="quiz-summary-login-link"
             onClick={onRegisterOrLoginClick}
          >
            <Button
              size='large'
              className="quiz-summary-login-button"
            >
              УВІЙТИ
            </Button>
          </a>
        </div>
      </Modal>
    </>
  )
    ;
};

export default QuizSummary;
