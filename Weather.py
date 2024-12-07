import tkinter as tk
import requests
import datetime as dt

def kelvinToCelsius(kelvin):
    return kelvin - 273.15

def get_weather():
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    apiKey = open("apikey.txt", 'r').read() #add your file name where you stored the api key
    CITY = city_entry.get()

    url = baseUrl + "appid=" + apiKey + "&q=" + CITY
    response = requests.get(url).json()

    if response.get("main"):
        temp_kelvin = response['main']['temp']
        temp_celsius = kelvinToCelsius(temp_kelvin)
        feels_like = kelvinToCelsius(response['main']['feels_like'])
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] 
                                               + response['timezone'])
        sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] 
                                              + response['timezone'])

        result_label.config(text=f"Weather in {CITY}:\n"
                                 f"Temperature: {temp_celsius:.2f}°C\n"
                                 f"Feels Like: {feels_like:.2f}°C\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Condition: {description}\n"
                                 f"Sunrise: {sunrise}\n"
                                 f"Sunset: {sunset}")
    else:
        result_label.config(text="City not found!")


root = tk.Tk()
root.title("Weather App")

window_width, window_height = 600, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

prompt_label = tk.Label(root, text="Enter City Name:", font=("Arial", 16))
prompt_label.pack(pady=20)

city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14), bg="#4CAF50", fg="white")
search_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14), justify="left", wraplength=500)
result_label.pack(pady=20)

root.mainloop()