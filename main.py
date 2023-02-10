import requests

# Your API key
api_key = "207ffa2b218540719501f16ea1551620"

# The endpoint URL
endpoint = "/Platform/Destiny2/Stats/Definition/"

# Add your API key to the headers
headers = {
    "X-API-Key": api_key
}

# Make the API request
response = requests.get(endpoint, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Do something with the data
    print(data)
else:
    # Handle the error
    print("An error occurred:", response.text)
