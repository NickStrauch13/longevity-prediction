import React, { useState } from 'react';

function LocationData({ topFeatures }) {

  const [zScoreToggles, setZScoreToggles] = useState({});

  const handleFeatureDivClick = (index) => {
    setZScoreToggles((prevToggles) => ({
      ...prevToggles,
      [index]: !prevToggles[index],
    }));
  };

  return (
    <div className="location-data-container">
      <h3>Top Contributing Factors</h3>

      <div className="all_top-features-container">
        {topFeatures.map((feature, index) => (
          <div
            key={index}
            className="location-data-single-feature-container"
            onClick={() => handleFeatureDivClick(index)}
          >
            <h2 className='location-data-feature-title'>{feature.feature}</h2>
            {zScoreToggles[index] ? (
              <p className='location-data-feature-data'>Z-Score: {feature.std_devs}</p>
            ) : (
              <p className='location-data-feature-data'>{feature.percentile} Percentile</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default LocationData;
