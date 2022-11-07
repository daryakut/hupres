import React, {useEffect, useState} from 'react';
import './static/style';
import {Button, Col, Popconfirm, Row} from "antd";
import {Link, useHistory} from 'react-router-dom';
import {deleteQuiz, getQuizzes} from "../api/quizzes_api";
import {CopyOutlined, DeleteOutlined, PlusOutlined} from "@ant-design/icons";

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
    <Row justify="center" className="fullscreen-div">
      <Col span={12} offset={6}>
        <div className="your-quizzes-title">Ваші анкети</div>
        <hr className="quizzes-hr-divider"/>
        {
          quizzes.map((quiz, index) => (
            <Link key={`quiz-${index}`} to={`/quiz/${quiz.token}`} style={{color: '#555'}}>
              <div className="quiz-container quiz-container-quizzes">
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
            className="quiz-container quiz-container-quizzes"
          >
            Додати нову анкету <PlusOutlined style={{margin: 10}}/>
          </div>
        </Link>
      </Col>
    </Row>
  );
};

export default Quizzes;
