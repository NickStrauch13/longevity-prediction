import React from 'react'

function LocationData({ locationData }) {
    return (
    <div className="location-data-container">

        <h3>Environmental Factors</h3>

        <div className="location-data-positives-and-negatives-container">
            <div className="positive-factors">
                {locationData.positives.map((positive, index) => (
                    <div className="location-data-positive-factor-div" key={index}>
                        <h4 className="location-data-factor-title">{positive.title}</h4>
                        <p className="location-data-factor-data">{positive.data}</p>
                    </div>
                ))}
            </div>

            <div className="negative-factors">
                {locationData.negatives.map((negative, index) => (
                <div className="location-data-negative-factor-div" key={index}>
                    <h4 className="location-data-factor-title">{negative.title}</h4>
                    <p className="location-data-factor-data">{negative.data}</p>
                </div>
                ))}
            </div>
        </div>
    </div>
    )
}

export default LocationData
