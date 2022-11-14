import streamlit as sl
import plotly.express as px
from backend import get_data

#Displaying the App
sl.title("Weather Forecast for the Next Few Days")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted data")
option = sl.selectbox("Select data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")

#Parsing the data
def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

if place:
    try:
        #Get the temperature/sky data
        d, t = get_data(place, days, option)

        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=d, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            sl.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condtions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condtions]
            sl.image(image_paths)

    except KeyError:
        sl.write("That place doesn't exist")