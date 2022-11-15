import React from 'react';
import {Col, Row} from "antd";

const QuizContainer = ({children}) => {
  return (
    <Row justify="center">
      <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
      <Col xs={22} sm={20} md={16} lg={12} xl={10}>
        {children}
      </Col>
    </Row>
  );
};

export default QuizContainer;
