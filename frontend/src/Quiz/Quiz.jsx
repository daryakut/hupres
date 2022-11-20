import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Checkbox, Input, Radio, Row, Select} from "antd";
import QueueAnim from "rc-queue-anim";
import {useHistory} from 'react-router-dom';
import {createQuiz, getNextQuizQuestion, getQuiz, submitQuizAnswer, updateQuiz} from "../api/quizzes_api";
import Text from "antd/es/typography/Text";
import {RightOutlined} from "@ant-design/icons";
import Header from "../Home/Header";
import QuizContainer from "./QuizContainer";

const HARD_TO_SAY_ANSWER_NAME = 'Затрудняюсь ответить'

const Quiz = ({match}) => {
  let history = useHistory();
  const [quiz, setQuiz] = useState(null);
  const [isMultipleChoice, setIsMultipleChoice] = useState(false);
  const [question, setQuestion] = useState(null);
  const [answers, setAnswers] = useState([]);
  const [isQuizComplete, setQuizComplete] = useState(false);
  const [pronounce, setPronounce] = useState(null);
  const [respondentName, setRespondentName] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedAnswers, setSelectedAnswers] = useState({});

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
      setIsMultipleChoice(response.is_multiple_choice);
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

  const submitAnswersAndFetchNext = async (answerNames) => {
    await submitQuizAnswer(quizQuestionToken, answerNames);
    await fetchNextQuestion();
  }

  const onSingleChoiceAnswerClick = async (answerName) => {
    await submitAnswersAndFetchNext([answerName]);
  }

  const onMultipleChoiceAnswerClick = async (answerName) => {
    if (answerName === HARD_TO_SAY_ANSWER_NAME) {
      setSelectedAnswers({[HARD_TO_SAY_ANSWER_NAME]: true});
    } else {
      setSelectedAnswers({...selectedAnswers, [answerName]: !selectedAnswers[answerName]});
    }
  }

  const onMultipleChoiceSubmitAnswersClick = async () => {
    await submitAnswersAndFetchNext(Object.keys(selectedAnswers));
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
          <QuizContainer>
            <div className="quiz-container quiz-container-summary" style={{marginTop: 300}}>
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
                  className="quiz-get-summary-button quiz-font-lg"
                  size='large'
                  disabled={!respondentName || !pronounce}
                  onClick={onGetResultsClick}
                >
                  Отримати Результат<RightOutlined/>
                </Button>
              </div>
            </div>
          </QuizContainer>
        </div>
      </>
    )
  }

  const displayQuestion = question?.question_display_name;

  return (
    <>
      <Header/>
      <div className="fullscreen-div">
        <QuizContainer>
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
              {isMultipleChoice ? (
                <>
                  {
                    answers.map((answer, index) => (
                      <Checkbox
                        key={`answer-${index}`}
                        className="quiz-answer"
                        checked={!!selectedAnswers[answer.answer_name]}
                        onChange={() => onMultipleChoiceAnswerClick(answer.answer_name)}>
                        {answer.answer_display_name}
                      </Checkbox>
                    ))
                  }
                  <Button
                    className="quiz-get-summary-button"
                    size='large'
                    disabled={!respondentName || !pronounce}
                    onClick={onMultipleChoiceSubmitAnswersClick}
                  >
                    Наступне питання
                  </Button>
                </>
              ) : (
                <Radio.Group onChange={onSingleChoiceAnswerClick} value={value}>
                  {
                    answers.map((answer, index) => (
                      <Radio
                        key={`answer-${index}`}
                        className="quiz-answer"
                        value={answer.answer_name}
                        onChange={() => onSingleChoiceAnswerClick(answer.answer_name)}>
                        {answer.answer_display_name}
                      </Radio>
                    ))
                  }
                </Radio.Group>
              )}
            </QueueAnim>
          </div>
        </QuizContainer>
      </div>
    </>
  );
};

export default Quiz;
