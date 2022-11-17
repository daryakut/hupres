import React from 'react';
import PropTypes from 'prop-types';
import ScrollOverPack from 'rc-scroll-anim/lib/ScrollOverPack';
import {Button, Icon} from 'antd';
import QueueAnim from 'rc-queue-anim';

export default function Page1({isMobile}) {
  return (
    <>
      {/*<ScrollOverPack id="page1" className="content-wrapper page">*/}
      <ScrollOverPack id="page1">
        <div className="page1-image" />
        <QueueAnim
          // type={isMobile ? 'bottom' : 'right'}
          type={'left'}
          className="text-wrapper page1-content"
          key="text1"
          leaveReverse
        >
          {/*<div style={{ width: '50%'}}> ya grut </div>*/}
          {/*<div style={{ width: '50%' }}> ya tut </div>*/}
          {/*<div className="text-wrapper page1-content">*/}
            <hr key="hr" className="landing-hr"/>
            <h2 key="h2" className="landing-font-lg">ЯК ЦЕ ПРАЦЮЄ</h2>
            <p key="p1" className="landing-font-sm">
              Консультант-психолог за допомогою штучного інтелекту на основі технології HUPRES дає вам змогу
              без проходження психологічних тестів отримати в режимі чату психологічну консультацію про себе та
              інших людей з будь-яких питань.
            </p>
            <p key="p2" className="landing-font-sm">
              Для отримання вірної інформації про характер людини технологія HUPRES використовує лише ваші
              знання про її зовнішній вигляд.
            </p>
          {/*</div>*/}
        </QueueAnim>
      </ScrollOverPack>
    </>
  );
}
Page1.propTypes = {
  isMobile: PropTypes.bool,
};
