import React from 'react';

function LifeExpecNum({ lifeExpectancy }) {

  const mapLifeExpectancyToColor = (value) => {
    const normalizedValue = (value - 50) / 50;
    const red = 255 - normalizedValue * 255;
    const green = normalizedValue * 255;
    return `rgb(${red}, ${green}, 0)`;
  };

  const sliderColor = mapLifeExpectancyToColor(lifeExpectancy);

  return (
    <div className="lifeexpec-number-container">
      <h3>National Average Life Expectancy</h3>
      <div className="lifeexpec-number-dot" style={{ backgroundColor: sliderColor }}>{lifeExpectancy}</div>
    </div>
  );
}

export default LifeExpecNum;
