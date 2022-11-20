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

  const selectedAnswersList = Object.keys(selectedAnswers).filter(answer => selectedAnswers[answer]);

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
    setSelectedAnswers({})
    await fetchNextQuestion();
  }

  const onSingleChoiceAnswerClick = async (answerName) => {
    setSelectedAnswers({[answerName]: true});
    await submitAnswersAndFetchNext([answerName]);
  }

  const onMultipleChoiceAnswerClick = async (answerName) => {
    if (answerName === HARD_TO_SAY_ANSWER_NAME) {
      setSelectedAnswers({[HARD_TO_SAY_ANSWER_NAME]: !selectedAnswers[HARD_TO_SAY_ANSWER_NAME]});
    } else {
      setSelectedAnswers({
        ...selectedAnswers,
        [answerName]: !selectedAnswers[answerName],
        [HARD_TO_SAY_ANSWER_NAME]: false,
      });
    }
  }

  const onMultipleChoiceSubmitAnswersClick = async () => {
    await submitAnswersAndFetchNext(selectedAnswersList);
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
                <Text className="quiz-input-label quiz-font-md">Імʼя чи нікнейм респондента</Text>
                <Input
                  className="quiz-input quiz-font-md"
                  placeholder="Імʼя респондента"
                  onChange={(e) => setRespondentName(e.target.value)}
                  value={respondentName}
                />
                <Text className="quiz-input-label quiz-font-md">Стать чи гендер респондента</Text>
                <Select
                  placeholder="Стать респондента"
                  className="quiz-input quiz-font-md"
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
                  disabled={!respondentName || !respondentName.trim() || !pronounce}
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
  const selectedAnswer = selectedAnswersList.length > 0 ? selectedAnswersList[0] : null

  return (
    <>
      <Header/>
      <div className="fullscreen-div">
        <QuizContainer>
          <div className="quiz-container" style={{marginTop}}>
            <QueueAnim
              type="left"
              delay={300}
            >
              <div key="question" className="quiz-question-container">
                <h2 className="quiz-question quiz-font-lg">{displayQuestion}</h2>
                <h5 className="quiz-font-md text-align-center quiz-question-clarification">
                  { isMultipleChoice ? "Виберіть всі що підходять" : "Виберіть один варіант" }
                </h5>
                <hr className="quiz-hr"/>
              </div>
              {isMultipleChoice ? (
                <QueueAnim
                  type="left"
                  delay={300}
                >
                  {
                    answers.map((answer, index) => (
                      <Checkbox
                        key={`answer-${index}`}
                        className="quiz-answer quiz-font-md"
                        checked={!!selectedAnswers[answer.answer_name]}
                        onChange={() => onMultipleChoiceAnswerClick(answer.answer_name)}>
                        {answer.answer_display_name}
                      </Checkbox>
                    ))
                  }
                  <div className="box-md" />
                  <Button
                    key="button"
                    className="quiz-get-summary-button quiz-font-md"
                    size='large'
                    disabled={selectedAnswersList.length === 0}
                    onClick={onMultipleChoiceSubmitAnswersClick}
                  >
                    Наступне питання
                  </Button>
                </QueueAnim>
              ) : (
                <Radio.Group value={selectedAnswer}>
                  <QueueAnim
                    type="left"
                    delay={300}
                  >
                  {
                    answers.map((answer, index) => (
                      <Radio
                        key={`answer-${index}`}
                        className="quiz-answer quiz-font-md"
                        value={answer.answer_name}
                        onChange={() => onSingleChoiceAnswerClick(answer.answer_name)}
                      >
                        {answer.answer_display_name}
                      </Radio>
                    ))
                  }
                  </QueueAnim>
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
