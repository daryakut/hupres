import React from 'react';
import './static/style';
import {enquireScreen} from 'enquire-js';
import {Col, Row} from "antd";
import QueueAnim from "rc-queue-anim";

let isMobile = false;
enquireScreen((b) => {
  isMobile = b;
});

class Quiz extends React.PureComponent {
  state = {
    isFirstScreen: true,
    isMobile,
  };

  componentDidMount() {
    enquireScreen((b) => {
      this.setState({
        isMobile: !!b,
      });
    });
  }

  onEnterChange = (mode) => {
    this.setState({
      isFirstScreen: mode === 'enter',
    });
  }

  render() {
    return (
      <Row justify="center" className="fullscreen-div">
        <Col span={12} offset={6}>
          <QueueAnim className="quiz-container" type="left" delay={300}>
            <div key="question" >
              <h2 className="quiz-question">Форма лица</h2>
              <hr className="landing-hr"/>
            </div>
            <div key="1" className="quiz-answer">Круглое лицо</div>
            <div key="2" className="quiz-answer">Вытянутый прямоугольник</div>
            <div key="3" className="quiz-answer">Большой треугольник</div>
            <div key="4" className="quiz-answer">Малый треугольник</div>
            <div key="5" className="quiz-answer">Широк прямоугольн "Квадрат"</div>
            <div key="6" className="quiz-answer">Затрудняюсь ответить</div>
          </QueueAnim>
        </Col>
      </Row>
    );
  }
}

export default Quiz;
