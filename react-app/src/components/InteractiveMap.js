import React from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps"

const geoUrl =
  "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json"

function InteractiveMap({ selectedCountry, onHover, onClick }) {
  
    const handleMouseEnter = (geo) => {
        const countryName = geo.properties.name;
        onHover(countryName);
    };
  
    const handleMouseLeave = () => {
        onHover(null);
    };

    const handleCountryClick = (geo) => {
        const countryName = geo.properties.name;
        onClick(countryName);
    }
  
    return (
      <ComposableMap className="composable-map">
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                onMouseEnter={() => handleMouseEnter(geo)} 
                onMouseLeave={handleMouseLeave}
                onClick={() => handleCountryClick(geo)}
                style={{
                  default: {
                    fill: selectedCountry === geo.properties.name ? "#0378cb" : "#D6D6DA",
                    outline: "none",
                    strokeWidth: 0.2, 
                    stroke: "#FFFFFF",
                    transition: "fill 0.2s"
                  },
                  hover: {
                    fill: "#3ca8f5",
                    outline: "none",
                    cursor: "pointer"
                  },
                  pressed: {
                    fill: "#0378cb",
                    outline: "none",
                  }
                }}
              />
            ))
          }
        </Geographies>
      </ComposableMap>
    );
  }
  
export default InteractiveMap;