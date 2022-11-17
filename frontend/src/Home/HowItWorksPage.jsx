import React from 'react';
import {BulbOutlined, FireOutlined, KeyOutlined, SmileOutlined} from "@ant-design/icons";

const SingleBulletPoint = ({children}) => (
  <div className="how-it-works-bullet-point-container">
    <p className="landing-font-md how-it-works-bullet-point">
      {children}
    </p>
  </div>
);

export default function HowItWorksPage() {
  return (
    <>
      <div id="how-it-works-page" className="how-it-works-page">
        <div className="person-model-image"/>
        <hr key="hr2" className="landing-hr"/>
        <h2 key="h2.2" className="landing-font-xl text-align-center full-width">ЯК ЦЕ ПРАЦЮЄ</h2>
        <div className="box-md"/>
        <div className="how-it-works-top-text-container">
          <p key="p2.1" className="landing-font-md landing-font-width-sm">
            Наші вчені, спираючись на наукові знання про конституцію людини, розробили унікальний метод
            визначення особистісних якостей людини тільки на основі фізичних параметрів будови її тіла.
          </p>
          <p key="p2.3" className="landing-font-md landing-font-width-sm">
            Сама ідея зв’язку будови тіла з фізіологічними та психологічними особливостями людини не нова.
            Розуміння цього глибокого зв'язку формувалося ще в стародавній та античної філософії. Сьогодні
            воно знаходить прояв у сучасній науці в психосоматичної медицини. Ця модна в останні роки галузь науки
            вивчає вплив психологічних чинників на розвиток соматичних, тобто тілесних захворювань.
          </p>
          <p key="p2.4" className="landing-font-md landing-font-width-sm">
            На відміну від стародавньої психосоматики, сучасна медицина та психологія займаються переважно
            вивченням причин захворювань та їх корекцією. Взаємодія тіла і психіки в стані умовного здоров'я
            таким чином стає поза інтересу, бо вважається, що тоді нема чого лікувати та коригувати.
          </p>
          <p key="p2.5" className="landing-font-md landing-font-width-sm">
            Але ж цей зв’язок між будовою тіла та психікою існує не тільки при захворюванні. В стані умовного
            здоров’я він нікуди не зникає! Саме на це і спирається HUPRES.
          </p>
          <p key="p2.6" className="landing-font-md landing-font-width-sm">
            При цьому, стверджуючі про прямий зв’язок між будовою тіла та психікою ми не маємо на увазі, що
            конкретна тілесна ознака, наприклад, форма носа, визначає конкретну психологічну рису, наприклад,
            міру агресивності. Саме сукупність тілесних ознак (загальний образ) відображає індивідуальну
            конституцію і відповідну сукупність рис характеру цієї людини.
          </p>
          <p key="p2.7" className="landing-font-md landing-font-width-sm">
            У процесі розробки цього методу ми спеціально зробили акцент на те, щоб його застосування було
            простим і легким для будь-якого користувача. Вам достатньо знати, як людина виглядає, а про решту
            подбають наш метод і сучасні технології. Використовуючи HUPRES ви зможете:
          </p>
        </div>
        <div className="how-it-works-text-container">
          <div className="practice-four-icons-container">
            <div className="practice-icon-pair-container">
              <SingleBulletPoint>
                <BulbOutlined className="practice-page-checkmark landing-font-lg"/>
                розуміти, чого варто чи не варто очікувати в будь-якій ситуації від конкретної людини;
              </SingleBulletPoint>
              <SingleBulletPoint>
                <SmileOutlined className="practice-page-checkmark landing-font-lg"/>
                знати, яку модель поведінки людина вибере, чим цей вибір мотивований, і що нею рухає;
              </SingleBulletPoint>
            </div>
            <div className="qualities-icon-pair-container">
              <SingleBulletPoint>
                <KeyOutlined className="practice-page-checkmark landing-font-lg"/>
                самостійно вирішити, як побудувати взаємодію з цією людиною, і зробити її ефективною та гармонійною;
              </SingleBulletPoint>
              <SingleBulletPoint>
                <FireOutlined className="practice-page-checkmark landing-font-lg"/>
                по-новому подивитися на себе, розкрити свій внутрішній потенціал для більш ефективної
                самореалізації.
              </SingleBulletPoint>
            </div>
          </div>
          <p key="p2.3" className="landing-font-md full-width">
            А завдяки технології штучного інтелекту чату HUPRES ви можете отримувати відповіді на практично
            буд-які запитання в режимі он-лайн. Таким чином, наша команда дає ключ до успішної самореалізації та
            взаємодії з іншими людьми. Це робить життя більш зрозумілим і комфортним без емоційних і
            матеріальних втрат.
          </p>
        </div>
      </div>
    </>
  );
}
