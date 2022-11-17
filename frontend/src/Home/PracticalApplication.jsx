import React from 'react';
import PropTypes from 'prop-types';
// {/*import ScrollOverPack from 'rc-scroll-anim/lib/ScrollOverPack';*/}
import QueueAnim from 'rc-queue-anim';
import {Col, Row} from "antd";

export default function PracticalApplication({isMobile}) {
  return (
    <>
      <div className="my-page">
        {/*<ScrollOverPack>*/}
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>
              {/*<QueueAnim*/}
              {/*  // type={isMobile ? 'bottom' : 'right'}*/}
              {/*  type={'left'}*/}
              {/*  className="text-wrapper page1-content-1"*/}
              {/*  key="text1"*/}
              {/*  leaveReverse*/}
              {/*>*/}
              <div className="text-wrapper page1-content">
                <hr key="hr1" className="landing-hr"/>
                <p key="p1.1" className="landing-font-md">
                  Консультант-психолог за допомогою штучного інтелекту на основі технології HUPRES дає вам змогу
                  без проходження психологічних тестів отримати в режимі чату психологічну консультацію про себе та
                  інших людей з будь-яких питань.
                </p>
                <p key="p.2" className="landing-font-md">
                  Для отримання вірної інформації про характер людини технологія HUPRES використовує лише ваші
                  знання про її зовнішній вигляд.
                </p>
              {/*</QueueAnim>*/}
              </div>
            </Col>
          </Row>
        {/*</ScrollOverPack>*/}
        {/*<ScrollOverPack>*/}
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>
              {/*<QueueAnim*/}
              {/*  // type={isMobile ? 'bottom' : 'right'}*/}
              {/*  type={'left'}*/}
              {/*  className="text-wrapper page1-content"*/}
              {/*  key="text1"*/}
              {/*  leaveReverse*/}
              {/*>*/}
              <div className="text-wrapper page1-content">
                <hr key="hr2" className="landing-hr"/>
                <h2 key="h2.2" className="landing-font-xl">ПРАКТИЧНЕ ЗАСТОСУВАННЯ</h2>
                <div key="p2.2" className="how-it-works-ul-wrapper">
                  <p key="p2.3" className="landing-font-sm">
                    Завдяки <strong>Human Personal Recognition System</strong> або HUPRES про людину можна
                    дізнатись дуже багато, використовуючи лише його фотографії або відео.
                  </p>
                  <p key="p2.4" className="landing-font-sm">
                    Більш того, HUPRES допомагає не тільки у пізнанні іншої людини, але й самого себе. Далеко не
                    кожен з нас здатен тверезо оцінити свої здібності та таланти.
                  </p>
                  <p key="p2.5" className="landing-font-sm">
                    У пошуках ідеального для себе образу життя, роботи, партнера або стосунків ми часто
                    помиляємося, підлаштовуючі себе під стереотипи, що нам зовсім невластиві.
                  </p>
                  <p key="p2.6" className="landing-font-sm">
                    Аналіз HUPRES дає конкретний та чіткий мануал дій, що оберігає від помилок.
                  </p>
                </div>
                </div>
              {/*</QueueAnim>*/}
            </Col>
          </Row>
        {/*</ScrollOverPack>*/}
      </div>
    </>
  );
}
PracticalApplication.propTypes = {
  isMobile: PropTypes.bool,
};
