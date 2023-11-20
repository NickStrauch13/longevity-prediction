import React from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import staticLifeExpectancyData from "../country_life_expectancy.json";

const geoUrl =
  "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json"

function InteractiveMap({ selectedCountry, onHover, onClick, colorOverlay}) {
  
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

    const mapLifeExpectancyToColor = (value) => {
      const normalizedValue = (value - 49) / (83 - 49);
    
      // Use a gradient with improved color values
      const red = Math.round(255 - normalizedValue * 180);
      const green = Math.round(normalizedValue * 200);
    
      return `rgb(${red}, ${green}, 0)`;
    };
  
    return (
      <ComposableMap className="composable-map">
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => {
              const countryName = geo.properties.name;
              const lifeExpectancy = staticLifeExpectancyData[countryName];

              return (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  onMouseEnter={() => onHover(countryName)}
                  onMouseLeave={() => onHover(null)}
                  onClick={() => onClick(countryName)}
                  style={{
                    default: {
                      fill:
                        selectedCountry === countryName
                          ? "#0378cb"
                          : colorOverlay && lifeExpectancy
                          ? mapLifeExpectancyToColor(lifeExpectancy)
                          : "#D6D6DA",
                      outline: "none",
                      strokeWidth: 0.2,
                      stroke: "#FFFFFF",
                      transition: "fill 0.2s",
                    },
                    hover: {
                      fill: "#3ca8f5",
                      outline: "none",
                      cursor: "pointer",
                    },
                    pressed: {
                      fill: "#0378cb",
                      outline: "none",
                    },
                  }}
                />
              );
            })
          }
        </Geographies>
      </ComposableMap>
    );
  }
  
export default InteractiveMap;