import React from 'react';
import {enquireScreen} from 'enquire-js';
import {Col, Row} from "antd";

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
      [
        <Row justify="space-evenly">
          <Col span={4}>col-4</Col>
          <Col span={4}>col-4</Col>
          <Col span={4}>col-4</Col>
          <Col span={4}>col-4</Col>
        </Row>
      ]
    );
  }
}

export default Quiz;