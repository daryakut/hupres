import React from 'react';

const BackgroundIcon = ({className, caption, description}) => (
  <div className="qualities-single-icon-container">
    <div className={`qualities-bg-icon ${className}`}/>
    <p className="landing-font-md color-blue text-align-center">
      {caption}
    </p>
    <p className="landing-font-sm color-blue text-align-center">
      {description}
    </p>
  </div>
);

export default function QualitiesPage() {
  return (
    <>
      <div className="qualities-page">
        <h5 key="p.2" className="qualities-page-title landing-font-lg color-blue text-align-center">
          НА ОСНОВІ СОМАТИЧНИХ (ТІЛЕСНИХ) ОЗНАК МЕТОДИКА ВИЗНАЧАЄ:
        </h5>
        <div className="qualities-four-icons-container">
          <div className="qualities-icon-pair-container">
            <BackgroundIcon
              className="bg-mozg_13"
              caption="СИЛЬНІ ТА СЛАБКІ СТОРОНИ ОСОБИСТОСТІ"
              description={"УСЕБІЧНО РОЗВИНЕНИХ ЛЮДЕЙ НЕ БУВАЄ, ЯК НЕ БУВАЄ І АБСОЛЮТНО СЛАБКИХ ОСОБИСТОСТЕЙ. " +
                "ОДНАК ОДНАКОВО КОРИСНО ЗНАТИ ПРО ВСІ СТОРІНИ ЛЮДИНИ."}
            />
            <BackgroundIcon
              className="bg-emoticon_06"
              caption="ТИП ПОВЕДІНКИ"
              description={"КОНСТИТУЦІЯ ЛЮДИНИ ВИЗНАЧАЄ ЙОГО ТЕМПЕРАМЕНТ В ЦІЛОМУ ТА " +
                "ПЕРЕВАЖНІ МОДЕЛІ ЙОГО ПОВЕДІНКИ."}
            />
          </div>
          <div className="qualities-icon-pair-container">
            <BackgroundIcon
              className="bg-pazzle_14"
              caption="ВЛАСТИВОСТІ КОНСТИТУЦІЇ ТА РЕАКЦІЇ НА РІЗНОМАНІТНІ СТИМУЛИ"
              description={"ЛЮДИ З РІЗНИМИ ТИПАМИ КОНСТИТУЦІЇ НА ОДИН ПОДРАЗНИК РЕАГУЮТЬ ПО-РІЗНОМУ."}
            />
            <BackgroundIcon
              className="bg-people_15"
              caption="СХИЛЬНОСТІ ДО ФІЗИЧНИХ ТА ПСИХІЧНИХ ПРОБЛЕМ"
              description={"ТИП КОНСТИТУЦІЇ ВИЗНАЧАЄ НАЙБІЛЬШ ЙМОВІРНІ ВАРІАНТИ ТІЛЕСНИХ І ПСИХОЛОГІЧНИХ " +
                "ПРОБЛЕМ. ЦЕ ВАЖЛИВО ДЛЯ ЇХ ПРОФІЛАКТИКИ."}
            />
          </div>
        </div>
      </div>
    </>
  );
}
