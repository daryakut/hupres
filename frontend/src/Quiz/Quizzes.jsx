import React, {useEffect, useState} from 'react';
import './static/style';
import {Col, Popconfirm, Row} from "antd";
import {Link, useHistory} from 'react-router-dom';
import {deleteQuiz, getQuizzes} from "../api/quizzes_api";
import {useUser} from "../User/UserProvider";
import {DeleteOutlined} from "@ant-design/icons";

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

  const deleteQuizAndRefresh = async function () {
    setQuizTokenToDelete(null);
    await deleteQuiz(quizTokenToDelete);
    await fetchQuizzes();
  }

  const onDeleteQuizClick = async function (quizToken) {
    setQuizTokenToDelete(quizToken);
  }

  const onCancelDeleteQuizClick = async function () {
    setQuizTokenToDelete(null);
  }

  return (
    <Row justify="center" className="fullscreen-div">
      <Col span={12} offset={6}>
        {
          quizzes.map((quiz, index) => (
            <div
              key={`quiz-${index}`}
              className="quiz-list-item"
            >
              <Link to={`/quiz/${quiz.token}`} style={{color: '#fff'}}>{quiz.subject_name ?? 'Без назви'}</Link>
              <Popconfirm
                title="Ви точно хочете видалити цю анкету?"
                onConfirm={deleteQuizAndRefresh}
                onCancel={onCancelDeleteQuizClick}
                okText="Так"
                cancelText="Ті"
              >
                <DeleteOutlined
                  onClick={() => onDeleteQuizClick(quiz.token)}
                />
              </Popconfirm>
            </div>
          ))
        }
      </Col>
    </Row>
  );
};

export default Quizzes;
