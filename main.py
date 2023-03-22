import requests
import json

activity_id = "12328300571"
membershipType = 3
displayName = "Icelord"
displayNameCode = 2239
4611686018448135534
2305843009265193154

# The endpoint URL
endpoint = "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/3/Icelord%232239/"
endpoint2 = "https://www.bungie.net/Platform/Destiny/2/Stats/GetMembershipIdByDisplayName/Icelord7749/"

# Add your API key to the headers
headers = {
    "X-API-Key": "207ffa2b218540719501f16ea1551620"

}

# Make the API request
response = requests.get(endpoint, headers=headers)

# Check the status code of the response

print(response)
parsed_response = json.loads(response.text)
print(parsed_response)
display_name = parsed_response["Response"][0]["displayName"]
print(display_name)

