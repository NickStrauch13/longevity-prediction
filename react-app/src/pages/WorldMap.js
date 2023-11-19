import React, {useState} from 'react'
import InteractiveMap from '../components/InteractiveMap';
import CountryStats from '../components/CountryStats';
import handleGetCountryData from '../apis/country_data';
import { AiOutlinePicture } from 'react-icons/ai';

function WorldMap() {

    const [hoveredCountry, setHoveredCountry] = useState(null);
    const [selectedCountry, setSelectedCountry] = useState(null);
    //const [selectedCountryData, setSelectedCountryData] = useState(null);
    const [selectedCountryData, setSelectedCountryData] = useState(
                                                                    {
                                                                        "life_expectancy": 77.9,
                                                                        "top_features": [
                                                                        {
                                                                            "feature": "Even societal power distribution",
                                                                            "percentile": 2.6,
                                                                            "std_devs": -1.946
                                                                        },
                                                                        {
                                                                            "feature": "Literacy rate, adult total",
                                                                            "percentile": 96.0,
                                                                            "std_devs": 1.755
                                                                        },
                                                                        {
                                                                            "feature": "Positivity",
                                                                            "percentile": 95.6,
                                                                            "std_devs": 1.71
                                                                        },
                                                                        {
                                                                            "feature": "Immunization, BCG",
                                                                            "percentile": 95.6,
                                                                            "std_devs": 1.703
                                                                        },
                                                                        {
                                                                            "feature": "Adversion to uncertainty",
                                                                            "percentile": 7.1,
                                                                            "std_devs": -1.466
                                                                        },
                                                                        {
                                                                            "feature": "Motivation",
                                                                            "percentile": 92.8,
                                                                            "std_devs": 1.464
                                                                        },
                                                                        {
                                                                            "feature": "Individualism",
                                                                            "percentile": 91.0,
                                                                            "std_devs": 1.343
                                                                        },
                                                                        {
                                                                            "feature": "Newborns protected against tetanus",
                                                                            "percentile": 84.3,
                                                                            "std_devs": 1.006
                                                                        }
                                                                        ]
                                                                    }
                                                                );

    const handleHoveredCountry = (country) => {
        setHoveredCountry(country);
    }

    const handleCountryClick = (clickedCountry) => {
        setSelectedCountry(clickedCountry);
        handleGetCountryData(clickedCountry, setSelectedCountryData);
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
