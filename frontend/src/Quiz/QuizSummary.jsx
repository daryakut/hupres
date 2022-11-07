import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Col, Input, Row, Select} from "antd";
import {useHistory} from 'react-router-dom';
import {askFreeFormQuestion, generateQuizSummary, getFreeFormQuestions} from "../api/quizzes_api";
import Text from "antd/es/typography/Text";
import {RightOutlined} from "@ant-design/icons";
import TextArea from "antd/es/input/TextArea";

const QuizSummary = ({match}) => {
  let history = useHistory();
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
      // setIsLoading(true);
      const freeFormAnswer = (await askFreeFormQuestion(quizToken, freeFormQuestion));
      console.log('freeFormAnswer', freeFormAnswer)
      setQuestions(questions.concat({question: freeFormQuestion, answer: freeFormAnswer}));
    } catch (error) {
      // setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  if (!summaries) {
    return null;
  }

  console.log('questions', questions)

  return (
    <div className="fullscreen-div-scrollable">
      <Row justify="center">
        <Col span={12} offset={6}>
          <div className="quiz-container quiz-container-summary">

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
            {
              questions.map((question, index) => (
                <div key={`question-${index}`}>
                  <Row key={`question-${index}`} justify="end">
                    <Col key={`summary-${index}`} span={8} offset={10}>
                      <h5 className="quiz-summary-content" style={{textAlign: 'right'}}>{question.question}</h5>
                    </Col>
                  </Row>
                  <Row key={`answer-${index}`} justify="start">
                    <Col key={`summary-${index}`} span={12} offset={6}>
                      <h5 className="quiz-summary-content">{question.answer}</h5>
                    </Col>
                  </Row>
                </div>
              ))
            }
          </div>
        </Col>
      </Row>

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
    </div>
  );
};

export default QuizSummary;
