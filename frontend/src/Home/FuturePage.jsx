import React from 'react';

export default function FuturePage() {
  return (
    <>
      <div id="future-page" className="future-page">
        <hr key="hr2" className="landing-hr"/>
        <h2 key="h2.2" className="landing-font-xl text-align-center full-width">ЯК МИ БАЧИМО МАЙБУТНЄ</h2>
        <div className="box-md"/>
        <p key="p2.1" className="landing-font-md landing-font-width-sm">
          З моменту зародження первісної концепції пройшло двадцять років. Два десятиріччя були присвячені
          пошукам та з’ясуванню чітких взаємозв’язків між конституцією людини та безліччю її психічних,
          розумових та фізіологічних аспектів.
        </p>
        <p key="p2.3" className="landing-font-md landing-font-width-sm">
          Результатом стала ціла низка продуктів, які, на наш погляд, можуть бути корисними як для звичайної
          людини, так і для професійного використання у різних галузях. Наприклад, в HR, менеджменті,
          психологічному консультуванні та терапії, освіті, психосоматичній медицині. Скрізь, де людина, її
          особистість має своє окреме значення.
        </p>
        <p key="p2.4" className="landing-font-md landing-font-width-sm">
          При тому ми розумієм, що задля повного комфорту та доступності для будь яких користувачів необхідно
          об’єднати нашу методику з сучасними технологіями. І в першу чергу ми активно працюємо над повною
          автоматизацією відповідей на ваші запитання із допомогою штучного інтелекту.
        </p>
        <div className="box-md"/>
        <h2 key="h2.5" className="landing-font-lg text-align-center full-width">
          СЕРЕД МАЙБУТНІХ НАШИХ ПРОДУКТІВ МИ БАЧИМО ТАКІ:
        </h2>

        <ul>
          <li className="landing-font-md">Допомога при депресії.</li>
          <li className="landing-font-md">Допомога при ПТСР (посттравматичному стресовому розладі).</li>
          <li className="landing-font-md">Соціальна реабілітація.</li>
          <li className="landing-font-md">Профорієнтація.</li>
          <li className="landing-font-md">Ефективне управління персоналом.</li>
          <li className="landing-font-md">Рекрутінг із врахуванням функціонального профілю робочого місця.</li>
          <li className="landing-font-md">Міжособистісні стосунки.</li>
        </ul>
      </div>
    </>
  );
}
