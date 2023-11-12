import React from 'react'

function CountryStats({ selectedCountry }) {
    return (
    <div className='country-stats-container'>
        {selectedCountry === null ? <h2 className="countrystats-placeholder-text">Select a Country</h2>: <h2 className="countrystats-selected-text">{selectedCountry}</h2>}

    </div>
    )
}

export default CountryStats
