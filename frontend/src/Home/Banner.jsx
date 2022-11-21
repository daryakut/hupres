import React from 'react';
import PropTypes from 'prop-types';
import ScrollElement from 'rc-scroll-anim/lib/ScrollElement';
import GitHubButton from 'react-github-button';
import {Button, Icon} from 'antd';
import QueueAnim from 'rc-queue-anim';
import {RightOutlined} from "@ant-design/icons";
import {Link} from "react-router-dom";

function typeFunc(a) {
  if (a.key === 'h2' || a.key === 'h5') {
    return 'left';
  } else if (a.key === 'button') {
    return 'bottom';
  }
  return 'right';
}

const Banner = ({ onEnterChange }) => {
  return (
    <section className="page banner-wrapper">
      <ScrollElement
        className="page"
        id="banner"
        onChange={({ mode }) => onEnterChange(mode)}
        playScale={0.9}
      >
        <QueueAnim className="banner-text-wrapper" type={typeFunc} delay={300} key="banner">
          <h2 key="h2" className="landing-font-xl landing-font-width-xl text-align-center">
            ШТУЧНИЙ КОНСУЛЬТАНТ-ПСИХОЛОГ, ЩО ЗАВЖДИ У ВАС ПІД РУКОЮ
          </h2>
          <hr key="hr" className="landing-hr"/>
          <h5 key="h5.2" className="landing-font-lg landing-font-width-lg text-align-center">
            НАШ УНІКАЛЬНИЙ МЕТОД ВИЗНАЧАЄ ХАРАКТЕР ЛЮДИНИ НА ОСНОВІ БУДОВИ ТІЛА
          </h5>
          <Link key="button" to="/quiz"><Button className="start-test-button">ПРОЙТИ ТЕСТ<RightOutlined /></Button></Link>
        </QueueAnim>
        <Icon type="down" className="down" />
      </ScrollElement>
    </section>
  );
}

export default Banner;
