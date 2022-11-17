import React from 'react';
import {CheckCircleOutlined} from "@ant-design/icons";


const SingleBulletPoint = ({children}) => (
  <div className="practice-bullet-point-container">
    <p className="landing-font-md practice-bullet-point">
      <CheckCircleOutlined className="practice-page-checkmark landing-font-lg"/>
      {children}
    </p>
  </div>
);

export default function PracticePage() {
  return (
    <>
      <div id="practice-page" className="practice-page">
        <div className="practice-page-top-header">
          <p key="p1.1" className="landing-font-md landing-font-width-xl text-align-center">
            Консультант-психолог за допомогою штучного інтелекту на основі технології HUPRES дає вам змогу
            без проходження психологічних тестів отримати в режимі чату психологічну консультацію про себе та
            інших людей з будь-яких питань.
          </p>
          <p key="p.2" className="landing-font-md landing-font-width-xl text-align-center">
            Для отримання вірної інформації про характер людини технологія HUPRES використовує лише ваші
            знання про її зовнішній вигляд.
          </p>
        </div>
        <div>
          <hr key="hr2" className="landing-hr"/>
          <h2 key="h2.2" className="landing-font-xl text-align-center full-width">ПРАКТИЧНЕ ЗАСТОСУВАННЯ</h2>
          <div className="practice-four-icons-container">
            <div className="practice-icon-pair-container">
              <SingleBulletPoint>
                Завдяки <strong>Human Personal Recognition System</strong> або HUPRES про людину можна
                дізнатись дуже багато, використовуючи лише його фотографії або відео.
              </SingleBulletPoint>
              <SingleBulletPoint>
                Більш того, HUPRES допомагає не тільки у пізнанні іншої людини, але й самого себе. Далеко не
                кожен з нас здатен тверезо оцінити свої здібності та таланти.
              </SingleBulletPoint>
            </div>
            <div className="qualities-icon-pair-container">
              <SingleBulletPoint>
                У пошуках ідеального для себе образу життя, роботи, партнера або стосунків ми часто
                помиляємося, підлаштовуючі себе під стереотипи, що нам зовсім невластиві.
              </SingleBulletPoint>
              <SingleBulletPoint>
                Аналіз HUPRES дає конкретний та чіткий мануал дій, що оберігає від помилок.
              </SingleBulletPoint>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
