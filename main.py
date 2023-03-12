import requests

url = "https://api.open-meteo.com/v1/forecast"

# Get user's location from ipinfo.io
ipinfo_url = "https://ipinfo.io/json"
response = requests.get(ipinfo_url)
if response.status_code == 200:
    ipinfo_data = response.json()
    lat, lon = ipinfo_data["loc"].split(",")
    location_name = ipinfo_data["city"]
    print(f"Detected location: {location_name}")
    print(lat, lon)
else:
    print("Error getting location:", response.status_code)
timezone = input("Enter timezone (e.g, America/St_Lucia, Asia/Tokyo, etc): ")
print("====")

#URL Parameters
params = {"latitude":lat, "longitude":lon, "hourly": "temperature_2m,weathercode","timezone": timezone}

response = requests.get(url, params=params)

#Main control flow
if response.status_code == 200:
    data = response.json()

    if data.get("hourly"):
        current_temp = data["hourly"]["temperature_2m"]
        weather_code = data["hourly"]["weathercode"]
        #Weather keys
        weather_desc = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: Light intensity",
    53: "Drizzle: Moderate intensity",
    55: "Drizzle: Dense intensity",
    56: "Freezing Drizzle: Light intensity",
    57: "Freezing Drizzle: Dense intensity",
    61: "Rain: Slight intensity",
    63: "Rain: Moderate intensity",
    65: "Rain: Heavy intensity",
    66: "Freezing Rain: Light intensity",
    67: "Freezing Rain: Heavy intensity",
    71: "Snow fall: Slight intensity",
    73: "Snow fall: Moderate intensity",
    75: "Snow fall: Heavy intensity",
    77: "Snow grains",
    80: "Rain showers: Slight intensity",
    81: "Rain showers: Moderate intensity",
    82: "Rain showers: Violent intensity",
    85: "Snow showers: Slight intensity",
    86: "Snow showers: Heavy intensity",
    95: "Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}       #Converting weather keys to readable text
        weather_text = weather_desc.get(int(weather_code[0]), "Unknown")

        #Printing weather data
        print("Current temperature at Saint Lucia is: ", current_temp[0], "degrees celsius")
        print("Weather is", weather_text, f"(code: {weather_code[0]})")
    else:
        print("No hourly data found.")
else: 
    print("Error:", response.status_code)
