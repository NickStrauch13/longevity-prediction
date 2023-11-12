import React, {useState} from 'react'
import InteractiveMap from '../components/InteractiveMap';
import CountryStats from '../components/CountryStats';

function WorldMap() {

    const [hoveredCountry, setHoveredCountry] = useState(null);
    const [selectedCountry, setSelectedCountry] = useState(null);

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
        <CountryStats selectedCountry={selectedCountry}/>
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
