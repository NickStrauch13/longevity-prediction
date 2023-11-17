import React from 'react'
import LifeExpecNum from './stats_components/LifeExpecNum'
import LocationData from './stats_components/LocationData'
import IndividualData from './stats_components/IndividualData'

function CountryStats({ selectedCountry, selectedCountryData}) {
    return (
    <div className='country-stats-container'>
        {selectedCountry === null ? <h1 className="countrystats-placeholder-text">Select a Country</h1>: <h1 className="countrystats-selected-text">{selectedCountry}</h1>}
        <div className="countrystats-data-container">
            <LifeExpecNum lifeExpectancy={selectedCountryData.life_expectancy}/>
            <LocationData locationData={selectedCountryData.location_data}/>
            <IndividualData />
        </div>
    </div>
    )
}

export default CountryStats
