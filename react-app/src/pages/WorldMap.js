import React, {useState} from 'react'
import InteractiveMap from '../components/InteractiveMap';

function WorldMap() {

    const [hoveredCountry, setHoveredCountry] = useState(null);

    const handleHoveredCountry = (country) => {
        setHoveredCountry(country);
    }

    const handleCountryClick = (clickedCountry) => {
        // TODO
        console.log('API request for:', clickedCountry);
      };

    return (
    <div className='worldmap-page-container'>
        <h1>{hoveredCountry}</h1>
        <InteractiveMap 
            className="worldmap"
            hoveredCountry={hoveredCountry} 
            onHover={handleHoveredCountry} 
            onClick={handleCountryClick}
        />
    </div>
    )
    }

export default WorldMap
