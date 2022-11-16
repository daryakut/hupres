import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Popconfirm} from "antd";
import {Link, useHistory} from 'react-router-dom';
import {deleteQuiz, getQuizzes} from "../api/quizzes_api";
import {DeleteOutlined, PlusOutlined} from "@ant-design/icons";
import Header from "../Home/Header";
import QuizContainer from "./QuizContainer";

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
