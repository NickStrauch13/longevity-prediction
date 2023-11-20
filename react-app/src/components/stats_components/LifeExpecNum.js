import React from 'react';

function LifeExpecNum({ lifeExpectancy }) {

  const mapLifeExpectancyToColor = (value) => {
    const normalizedValue = (value - 49) / (83 - 49);
  
    // Use a gradient with improved color values
    const red = Math.round(255 - normalizedValue * 180); 
    const green = Math.round(normalizedValue * 200);
  
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
