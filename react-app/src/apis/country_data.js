
const handleGetCountryData = async (country, setSelectedCountryData) => {
    const url = "http://127.0.0.1:5000/get_country_data"

    try {
        const response = await fetch(url, {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'country': country
            }
        });

        const data = await response.json();
        setSelectedCountryData(data);
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}

export default handleGetCountryData;