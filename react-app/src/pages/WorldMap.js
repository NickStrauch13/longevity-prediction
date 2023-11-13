import React, {useState} from 'react'
import InteractiveMap from '../components/InteractiveMap';
import CountryStats from '../components/CountryStats';

function WorldMap() {

    const [hoveredCountry, setHoveredCountry] = useState(null);
    const [selectedCountry, setSelectedCountry] = useState(null);
    //const [selectedCountryData, setSelectedCountryData] = useState(null);
    const [selectedCountryData, setSelectedCountryData] = useState({"life_expectancy": 81,
                                                                    "location_data": {
                                                                        "positives": [
                                                                            {
                                                                                "title": "Happiness",
                                                                                "data": "The happiness score of the country is 6.5",
                                                                            },
                                                                            {
                                                                                "title": "GDP per Catpita",
                                                                                "data": "The GDP per capita of the country is $40,000",
                                                                            }
                                                                        ],
                                                                        "negatives": [
                                                                            {
                                                                                "title": "Access to Healthcare",
                                                                                "data": "The country has a score of 0.5 for access to healthcare",
                                                                            }
                                                                        ]
                                                                    }
                                                                });

    const handleHoveredCountry = (country) => {
        setHoveredCountry(country);
    }

    const handleCountryClick = (clickedCountry) => {
        // TODO
        setSelectedCountry(clickedCountry);
        console.log('API request for:', clickedCountry);
      };

    return (
    <div className='worldmap-page-container'>
        <CountryStats selectedCountry={selectedCountry} selectedCountryData={selectedCountryData}/>
        <div className='worldmap-map-and-text-container'>
            {hoveredCountry === null ? 
                <h1 className="worldmap-placeholder-text">{selectedCountry=== null ? "Select a Country" : selectedCountry}</h1> : 
                <h1 className="worldmap-country-text">{hoveredCountry}</h1>}
            <InteractiveMap 
                className="worldmap"
                selectedCountry={selectedCountry}
                onHover={handleHoveredCountry} 
                onClick={handleCountryClick}
            />
        </div>
        
    </div>
    )
    }

export default WorldMap
