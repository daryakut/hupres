import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Col, Input, Row, Select} from "antd";
import {useHistory} from 'react-router-dom';
import {askFreeFormQuestion, generateQuizSummary, getFreeFormQuestions} from "../api/quizzes_api";
import Text from "antd/es/typography/Text";
import {CopyOutlined, LoadingOutlined, RightOutlined} from "@ant-design/icons";
import TextArea from "antd/es/input/TextArea";
import {useUser} from "../User/UserProvider";
import Header from "../Home/Header";

const QuizSummary = ({match}) => {
  let history = useHistory();
  const {user} = useUser();
  const [summaries, setSummaries] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [freeFormQuestion, setFreeFormQuestion] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const quizToken = match.params.quizToken;

  useEffect(() => {
    fetchQuizSummary();
  }, [quizToken]);

  const fetchQuizSummary = async () => {
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
      // setIsLoading(false);
    }
  };

  const onAskFreeFormQuestionClick = async () => {
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
      setFreeFormQuestion(null);
      await onAskFreeFormQuestionClick();
    }
  }

  if (!summaries) {
    return null;
  }

  // Only logged in users can chat with AI
  const isLoggedIn = !!user;

  return (
    <>
      <Header key="header"/>
      {/*<div style={{height: 80}}/>*/}
      <div className="fullscreen-div-scrollable">
        <Row justify="center">
          <Col span={12} offset={6}>
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

            {isLoggedIn ? (
              <div style={{height: 100}}/>
            ) : null}
          </Col>
        </Row>

        {isLoggedIn ? (
          <div className="free-form-question-input-container">
            <div className="free-form-question-input-container-fade"/>
            <div className="free-form-question-input-container-white">
              <Row>
                <Col span={24} offset={0}>
                  <Text className="free-form-question-input-label">
                    Ви також можете запитати що вас цікавить стосовно респондента у нашого AI помічника
                  </Text>
                </Col>
              </Row>
              <Row style={{marginTop: 6}}>
                <Col span={20} offset={0}>
                  {/*<Input*/}
                  <TextArea rows={2}
                            className="free-form-question-input"
                            placeholder="Як мотивуваті цього респондента?"
                            value={freeFormQuestion}
                            onChange={(e) => setFreeFormQuestion(e.target.value)}
                            onKeyDown={onFreeFormQuestionKeyDown}
                  />
                </Col>
                <Col span={4}>
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
            </div>
          </div>
        ) : null}
      </div>
    </>
  )
    ;
};

export default QuizSummary;
