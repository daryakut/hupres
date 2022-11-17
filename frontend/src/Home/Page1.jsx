import React from 'react';
import PropTypes from 'prop-types';
import ScrollOverPack from 'rc-scroll-anim/lib/ScrollOverPack';
import QueueAnim from 'rc-queue-anim';
import {Col, Row} from "antd";

export default function Page1({isMobile}) {
  return (
    <>
      <div id="page1">
        <ScrollOverPack>
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>
              <QueueAnim
                // type={isMobile ? 'bottom' : 'right'}
                type={'left'}
                className="text-wrapper page1-content-1"
                key="text1"
                leaveReverse
              >
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
              </QueueAnim>
            </Col>
          </Row>
        </ScrollOverPack>
        <div className="page1-image"/>
        <ScrollOverPack>
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>

              <QueueAnim
                // type={isMobile ? 'bottom' : 'right'}
                type={'left'}
                className="text-wrapper page1-content"
                key="text1"
                leaveReverse
              >
                <hr key="hr2" className="landing-hr"/>
                <h2 key="h2.2" className="landing-font-xl">ЯК ЦЕ ПРАЦЮЄ</h2>
                <p key="p2.1" className="landing-font-sm">
                  Наші вчені, спираючись на наукові знання про конституцію людини, розробили унікальний метод
                  визначення особистісних якостей людини тільки на основі фізичних параметрів будови її тіла.
                </p>
                <p key="p2.3" className="landing-font-sm">
                  Сама ідея зв’язку будови тіла з фізіологічними та психологічними особливостями людини не нова.
                  Розуміння цього глибокого зв'язку формувалося ще в стародавній та античної філософії. Сьогодні
                  воно знаходить прояв у сучасній науці в психосоматичної медицини. Ця модна в останні роки галузь науки
                  вивчає вплив психологічних чинників на розвиток соматичних, тобто тілесних захворювань.
                </p>
                <p key="p2.4" className="landing-font-sm">
                  На відміну від стародавньої психосоматики, сучасна медицина та психологія займаються переважно
                  вивченням причин захворювань та їх корекцією. Взаємодія тіла і психіки в стані умовного здоров'я
                  таким чином стає поза інтересу, бо вважається, що тоді нема чого лікувати та коригувати.
                </p>
                <p key="p2.5" className="landing-font-sm">
                  Але ж цей зв’язок між будовою тіла та психікою існує не тільки при захворюванні. В стані умовного
                  здоров’я він нікуди не зникає! Саме на це і спирається HUPRES.
                </p>
                <p key="p2.6" className="landing-font-sm">
                  При цьому, стверджуючі про прямий зв’язок між будовою тіла та психікою ми не маємо на увазі, що
                  конкретна тілесна ознака, наприклад, форма носа, визначає конкретну психологічну рису, наприклад,
                  міру агресивності. Саме сукупність тілесних ознак (загальний образ) відображає індивідуальну
                  конституцію і відповідну сукупність рис характеру цієї людини.
                </p>
              </QueueAnim>
            </Col>
          </Row>
          {/*</ScrollOverPack>*/}
          {/*<ScrollOverPack>*/}
          <Row>
            <Col xs={1} sm={2} md={4} lg={6} xl={7}/>
            <Col xs={22} sm={20} md={16} lg={12} xl={10}>

              <QueueAnim
                // type={isMobile ? 'bottom' : 'right'}
                type={'left'}
                className="text-wrapper page1-content"
                key="text1"
                leaveReverse
              >
                {/*<hr key="hr2" className="landing-hr"/>*/}
                {/*<h2 key="h2.2" className="landing-font-xl">ЯК ЦЕ ПРАЦЮЄ</h2>*/}
                <p key="p2.1" className="landing-font-sm">
                  У процесі розробки цього методу ми спеціально зробили акцент на те, щоб його застосування було
                  простим і легким для будь-якого користувача. Вам достатньо знати, як людина виглядає, а про решту
                  подбають наш метод і сучасні технології. Використовуючи HUPRES ви зможете:
                </p>
                <div key="p2.2" className="how-it-works-ul-wrapper">
                  <p key="p2.3" className="landing-font-sm">
                    розуміти, чого варто чи не варто очікувати в будь-якій ситуації від конкретної людини;
                  </p>
                  <p key="p2.4" className="landing-font-sm">
                    знати, яку модель поведінки людина вибере, чим цей вибір мотивований, і що нею рухає;
                  </p>
                  <p key="p2.5" className="landing-font-sm">
                    самостійно вирішити, як побудувати взаємодію з цією людиною, і зробити її ефективною та гармонійною;
                  </p>
                  <p key="p2.6" className="landing-font-sm">
                    по новому подивитися на себе, розкрити свій внутрішній потенціал для більш ефективної
                    самореалізації.
                  </p>
                </div>
                <p key="p2.3" className="landing-font-sm">
                  А завдяки технології штучного інтелекту чату HUPRES ви можете отримувати відповіді на практично
                  буд-які запитання в режимі он-лайн. Таким чином, наша команда дає ключ до успішної самореалізації та
                  взаємодії з іншими людьми. Це робить життя більш зрозумілим і комфортним без емоційних і
                  матеріальних втрат.
                </p>
              </QueueAnim>
            </Col>
          </Row>
        </ScrollOverPack>
      </div>
    </>
  );
}
Page1.propTypes = {
  isMobile: PropTypes.bool,
};
