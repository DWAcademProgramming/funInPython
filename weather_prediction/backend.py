import requests
API_Key = "07c1c5cf0e247afa74f169dfc5600c3c"

def get_data(place, forecast_days=None):
    url = "api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Chicago", forecast_days=3))