import React, {useState} from 'react'
import InteractiveMap from '../components/InteractiveMap';
import CountryStats from '../components/CountryStats';
import handleGetCountryData from '../apis/country_data';
import { AiOutlinePicture } from 'react-icons/ai';

function WorldMap() {

    const [hoveredCountry, setHoveredCountry] = useState(null);
    const [selectedCountry, setSelectedCountry] = useState(null);
    const [selectedCountryData, setSelectedCountryData] = useState(null);
    const [colorOverlay, setColorOverlay] = useState(true);

    const handleHoveredCountry = (country) => {
        setHoveredCountry(country);
    }

    const handleCountryClick = (clickedCountry) => {
        setSelectedCountry(clickedCountry);
        handleGetCountryData(clickedCountry, setSelectedCountryData);
    };   
    
    const handleColorOverlayToggle = () => {
        setColorOverlay(!colorOverlay);
    }

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
                colorOverlay={colorOverlay}
            />
            <button className='toggle-button' onClick={handleColorOverlayToggle}>
                Toggle Color Overlay
            </button>
        </div>
        
    </div>
    )
    }

export default WorldMap
