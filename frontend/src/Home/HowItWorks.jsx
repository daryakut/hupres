import React from 'react';
import PropTypes from 'prop-types';
// {/*import ScrollOverPack from 'rc-scroll-anim/lib/ScrollOverPack';*/}
import QueueAnim from 'rc-queue-anim';
import {Col, Row} from "antd";

export default function HowItWorks({isMobile}) {
  return (
    <>
      <div className="my-page">
        <div className="page1-image"/>
        {/*<ScrollOverPack>*/}
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>
              <div className="text-wrapper page1-content">
              {/*<QueueAnim*/}
              {/*  // type={isMobile ? 'bottom' : 'right'}*/}
              {/*  type={'left'}*/}
              {/*  className="text-wrapper page1-content"*/}
              {/*  key="text1"*/}
              {/*  leaveReverse*/}
              {/*>*/}
                <hr key="hr2" className="landing-hr"/>
                <h2 key="h2.2" className="landing-font-xl landing-font-width-xl">ЯК ЦЕ ПРАЦЮЄ</h2>
                <p key="p2.1" className="landing-font-sm landing-font-width-sm">
                  Наші вчені, спираючись на наукові знання про конституцію людини, розробили унікальний метод
                  визначення особистісних якостей людини тільки на основі фізичних параметрів будови її тіла.
                </p>
                <p key="p2.3" className="landing-font-sm landing-font-width-sm">
                  Сама ідея зв’язку будови тіла з фізіологічними та психологічними особливостями людини не нова.
                  Розуміння цього глибокого зв'язку формувалося ще в стародавній та античної філософії. Сьогодні
                  воно знаходить прояв у сучасній науці в психосоматичної медицини. Ця модна в останні роки галузь науки
                  вивчає вплив психологічних чинників на розвиток соматичних, тобто тілесних захворювань.
                </p>
                <p key="p2.4" className="landing-font-sm landing-font-width-sm">
                  На відміну від стародавньої психосоматики, сучасна медицина та психологія займаються переважно
                  вивченням причин захворювань та їх корекцією. Взаємодія тіла і психіки в стані умовного здоров'я
                  таким чином стає поза інтересу, бо вважається, що тоді нема чого лікувати та коригувати.
                </p>
                <p key="p2.5" className="landing-font-sm landing-font-width-sm">
                  Але ж цей зв’язок між будовою тіла та психікою існує не тільки при захворюванні. В стані умовного
                  здоров’я він нікуди не зникає! Саме на це і спирається HUPRES.
                </p>
                <p key="p2.6" className="landing-font-sm landing-font-width-sm">
                  При цьому, стверджуючі про прямий зв’язок між будовою тіла та психікою ми не маємо на увазі, що
                  конкретна тілесна ознака, наприклад, форма носа, визначає конкретну психологічну рису, наприклад,
                  міру агресивності. Саме сукупність тілесних ознак (загальний образ) відображає індивідуальну
                  конституцію і відповідну сукупність рис характеру цієї людини.
                </p>
              {/*</QueueAnim>*/}
              </div>
            </Col>
          </Row>
          {/*/!*</ScrollOverPack>*!/*/}
          {/*/!*<ScrollOverPack>*!/*/}
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>
              <div className="text-wrapper page1-content">
              {/*<QueueAnim*/}
              {/*  // type={isMobile ? 'bottom' : 'right'}*/}
              {/*  type={'left'}*/}
              {/*  className="text-wrapper page1-content"*/}
              {/*  key="text1"*/}
              {/*  leaveReverse*/}
              {/*>*/}
                {/*<hr key="hr2" className="landing-hr"/>*/}
                {/*<h2 key="h2.2" className="landing-font-xl landing-font-width-xl">ЯК ЦЕ ПРАЦЮЄ</h2>*/}
                <p key="p2.1" className="landing-font-sm landing-font-width-sm">
                  У процесі розробки цього методу ми спеціально зробили акцент на те, щоб його застосування було
                  простим і легким для будь-якого користувача. Вам достатньо знати, як людина виглядає, а про решту
                  подбають наш метод і сучасні технології. Використовуючи HUPRES ви зможете:
                </p>
                <div key="p2.2" className="how-it-works-ul-wrapper">
                  <p key="p2.3" className="landing-font-sm landing-font-width-sm">
                    розуміти, чого варто чи не варто очікувати в будь-якій ситуації від конкретної людини;
                  </p>
                  <p key="p2.4" className="landing-font-sm landing-font-width-sm">
                    знати, яку модель поведінки людина вибере, чим цей вибір мотивований, і що нею рухає;
                  </p>
                  <p key="p2.5" className="landing-font-sm landing-font-width-sm">
                    самостійно вирішити, як побудувати взаємодію з цією людиною, і зробити її ефективною та гармонійною;
                  </p>
                  <p key="p2.6" className="landing-font-sm landing-font-width-sm">
                    по новому подивитися на себе, розкрити свій внутрішній потенціал для більш ефективної
                    самореалізації.
                  </p>
                </div>
                <p key="p2.3" className="landing-font-sm landing-font-width-sm">
                  А завдяки технології штучного інтелекту чату HUPRES ви можете отримувати відповіді на практично
                  буд-які запитання в режимі он-лайн. Таким чином, наша команда дає ключ до успішної самореалізації та
                  взаємодії з іншими людьми. Це робить життя більш зрозумілим і комфортним без емоційних і
                  матеріальних втрат.
                </p>
              </div>
              {/*</QueueAnim>*/}
            </Col>
          </Row>
        {/*</ScrollOverPack>*/}
      </div>
    </>
  );
}
HowItWorks.propTypes = {
  isMobile: PropTypes.bool,
};
