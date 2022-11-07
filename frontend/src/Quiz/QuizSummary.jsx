import React, {useEffect, useState} from 'react';
import './static/style';
import {Col, Row} from "antd";
import {useHistory} from 'react-router-dom';
import {askFreeFormQuestion, generateQuizSummary} from "../api/quizzes_api";

const QuizSummary = ({match}) => {
  let history = useHistory();
  const [summaries, setSummaries] = useState(null);
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
      // await askFreeFormQuestion(quizToken, "Как лучше всего смотивировать сотрудника?");
    } catch (error) {
      // setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  if (!summaries) {
    return null;
  }

  return (
    <Row justify="center" className="quiz-summary-screen">
      {
        summaries.map((summary, index) => (
          <Col key={`summary-${index}`} span={12} offset={6}>
            <h2 className="quiz-summary-title">{summary.title}</h2>
            <h5 className="quiz-summary-content">{summary.summary}</h5>
          </Col>
        ))
      }
    </Row>
  );
};

export default QuizSummary;
