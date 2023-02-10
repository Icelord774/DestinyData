import requests

activity_id = "12328300571"

# The endpoint URL
endpoint = f"https://www.bungie.net/Platform/Destiny2/Stats/PostGameCarnageReport/{activity_id}/"

# Add your API key to the headers
headers = {
    "X-API-Key": "207ffa2b218540719501f16ea1551620"
}

# Make the API request
response = requests.get(endpoint, headers=headers).json()

# Check the status code of the response

# Do something with the data
teams = response["Response"]["entries"]

for team in teams:

    score = team["score"]

    print("Score:", score)
    print("Players:")

    # END FOR


