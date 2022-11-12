import streamlit
import streamlit as sl
import pandas as pd

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/photo.png", width=500)

with col2:
    sl.title('Random Asshole')
    content = """
    This is complete and total bullshit and I'm being laughably childish
    """

    sl.write(content)

comment = """
    These are some of the projects I've built. 
"""

sl.write(comment)

col3, emptyCol, col4 = sl.columns([1.5, .5, 1.5])
df = pd.read_csv('data.csv', sep=";")
with col3:
    for index, row in df[:10].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")