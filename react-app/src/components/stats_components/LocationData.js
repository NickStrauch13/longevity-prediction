import React from 'react'

function LocationData({ topFeatures }) {
    return (
    <div className="location-data-container">

        <h3>Top Contributing Factors</h3>

        <div className="all_top-features-container">
            {topFeatures.map((feature, index) => (
            <div key={index} className="location-data-single-feature-container">
                <h2 className='location-data-feature-title'>{feature.feature}</h2>
                <p className='location-data-feature-data'>{feature.percentile} Percentile</p>
            </div>
            ))}
      </div>
    </div>
    )
}

export default LocationData
