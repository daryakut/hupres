import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Popconfirm} from "antd";
import {Link, useHistory} from 'react-router-dom';
import {deleteQuiz, getQuizzes} from "../api/quizzes_api";
import {DeleteOutlined, PlusOutlined} from "@ant-design/icons";
import Header from "../Home/Header";
import QuizContainer from "./QuizContainer";
import dayjs from 'dayjs';

const formatUtcStringToLocal = (utcString) => {
  const eventDate = dayjs(utcString);
  const currentDate = dayjs();

  const time = eventDate.format('HH:mm');
  // Check if the event happened today
  if (eventDate.isSame(currentDate, 'day')) {
    // Format to local hours and minutes
    return `Сьогодні ${time}`;
  }
  const date = eventDate.format('DD.MM');
  // Format to the local day
  return `${date} ${time}`;
  // const eventDate = new Date(utcString);
  // const currentDate = new Date();
  //
  // // Extracting components of the dates in local timezone
  // const eventYear = eventDate.getFullYear();
  // const eventMonth = eventDate.getMonth();
  // const eventDay = eventDate.getDate();
  //
  // const currentYear = currentDate.getFullYear();
  // const currentMonth = currentDate.getMonth();
  // const currentDay = currentDate.getDate();
  //
  // const time = `${eventDate.getHours().toString()}:${eventDate.getMinutes().toString()}`;
  // // Check if the event happened today
  // if (eventYear === currentYear && eventMonth === currentMonth && eventDay === currentDay) {
  //   // Format to hours and minutes in local timezone
  //   return `Сьогодні ${time}`;
  // } else {
  //   // Format to the day (e.g., '16') in local timezone
  //   return `${eventDay}.${currentMonth} ${time}`;
  // }
};

const Quizzes = ({match}) => {
  let history = useHistory();

  // const {user} = useUser();
  // if (!user) {
  //   history.replace('/');
  // }

  const [quizTokenToDelete, setQuizTokenToDelete] = useState(null);

  const [quizzes, setQuizzes] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchQuizzes();
  }, []);

  const fetchQuizzes = async () => {
    try {
      // setIsLoading(true);
      const quizzes = await getQuizzes();
      setQuizzes(quizzes);
    } catch (error) {
      // setError(error);
    } finally {
      // setIsLoading(false);
    }
  };

  const deleteQuizAndRefresh = async function (event) {
    event.stopPropagation();
    setQuizTokenToDelete(null);
    await deleteQuiz(quizTokenToDelete);
    await fetchQuizzes();
  }

  const onDeleteQuizClick = async function (quizToken) {
    setQuizTokenToDelete(quizToken);
  }

  const onCancelDeleteQuizClick = async function (event) {
    event.stopPropagation();
    setQuizTokenToDelete(null);
  }

  return (
    <>
      <Header key="header"/>
      <div className="fullscreen-div"/>
      <div className="fullscreen-div-scrollable">
        <QuizContainer>
          <div className="your-quizzes-title quiz-font-xl">Ваші анкети</div>
          {quizzes.length > 0 ? (
            <hr className="quizzes-hr-divider"/>
          ) : null}
          {
            quizzes.map((quiz, index) => (
              <Link key={`quiz-${index}`} to={`/quiz/${quiz.token}`} style={{color: '#555'}}>
                <div className="quiz-container quiz-container-quizzes quiz-font-lg">
                  {quiz.subject_name ?? 'Не завершено'}
                  <div className="quiz-container-time-and-delete">
                    {formatUtcStringToLocal(quiz.created_at)}
                    <Popconfirm
                      title="Ви точно хочете видалити цю анкету?"
                      onConfirm={(e) => deleteQuizAndRefresh(e)}
                      onCancel={(e) => onCancelDeleteQuizClick(e)}
                      okText="Так"
                      cancelText="Ні"
                    >
                      <Button
                        className="copy-to-clipboard-button"
                        onClick={() => onDeleteQuizClick(quiz.token)}
                      ><DeleteOutlined/></Button>
                    </Popconfirm>
                  </div>
                </div>
              </Link>
            ))
          }
          <hr className="quizzes-hr-divider"/>
          <Link to={`/quiz`} style={{color: '#555'}}>
            <div
              className="quiz-container quiz-container-quizzes quiz-font-lg"
            >
              Додати нову анкету <PlusOutlined style={{margin: 10}}/>
            </div>
          </Link>
        </QuizContainer>
      </div>
    </>
  );
};

export default Quizzes;
