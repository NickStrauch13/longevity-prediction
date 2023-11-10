import React, { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps"

const geoUrl =
  "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json"

function InteractiveMap() {
    const [hoveredCountry, setHoveredCountry] = useState(null);
  
    const handleMouseEnter = (geo) => {
      setHoveredCountry(geo.properties.name);
      console.log("Hovered Country:", geo.properties.name);
    };
  
    const handleMouseLeave = () => {
      setHoveredCountry(null);
    };
  
    return (
      <ComposableMap>
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                onMouseEnter={() => handleMouseEnter(geo)} // Pass the geo object to handleMouseEnter
                onMouseLeave={handleMouseLeave}
                style={{
                  default: {
                    fill: hoveredCountry === geo.properties.name ? "#FF5722" : "#D6D6DA",
                    outline: "none",
                  },
                  hover: {
                    fill: "#FF5722",
                    outline: "none",
                  },
                  pressed: {
                    fill: "#FF5722",
                    outline: "none",
                  },
                }}
              />
            ))
          }
        </Geographies>
      </ComposableMap>
    );
  }
  
export default InteractiveMap;