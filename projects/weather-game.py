# Include the current weather into your game mechanics.

import requests

user_location = input("Enter the name of city you live: ").lower()

location_url=f"https://www.metaweather.com/api/location/search/?query={user_location}"

id_response = requests.get(location_url)
data=id_response.json()
woeid=data[0]["woeid"]
# print(woeid)

URL = f"https://www.metaweather.com/api/location/{woeid}"

response = requests.get(URL)
loc_data=response.json() 
# print(loc_data)
current_weather = loc_data["consolidated_weather"][0]["weather_state_name"]
print(f"The current weather in your area is {current_weather}.")

user_guess = float(input("What do you think is the current temperature in Celcius?: "))

current_temp = round((loc_data["consolidated_weather"][0]["the_temp"]),1)
# print(current_temp)

if user_guess == current_temp:
    print("Spot on!")
elif user_guess > current_temp:
    print(f"Your body is feeling hotter than the actual temp {current_temp} degrees💩")
else:
    difference = round((current_temp - user_guess),1)
    print(f"Nah, it's much warmer👅 {difference} degrees warmer. {current_temp} degrees now.")


