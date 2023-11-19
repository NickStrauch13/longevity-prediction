
const handleGetCountryData = async (country, setSelectedCountryData) => {
    const url = `http://127.0.0.1:5000/get_country_data?country=${country}`;

    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
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