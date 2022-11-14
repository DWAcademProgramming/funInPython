import streamlit as sl
import plotly.express as px

sl.title("Weather Forecast for the Next Few Days")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted data")
option = sl.selectbox("Select data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
sl.plotly_chart(figure)