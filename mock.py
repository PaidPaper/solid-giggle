# mock_script.py

import requests
from unittest.mock import patch

def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

if __name__ == "__main__":
    url = "https://api.example.com/data"
    print("Fetching data from API...")
    data = fetch_data_from_api(url)
    print(data)

# Unit test section (mock example)

def test_fetch_data_from_api():
    mock_response = {"id": 1, "name": "Mock Item", "value": 100}
    
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mock_response

        result = fetch_data_from_api("https://mockapi.test/data")
        
        assert result == mock_response
        print("Test passed: API data mocked successfully")
