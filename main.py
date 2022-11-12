import streamlit as sl

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/photo.png", width=500)

with col2:
    sl.title('Random Asshole')
    content = """
    This is complete and total bullshit and I'm being laughably childish
    """
    comment = """
        These are some of the projects I've built. 
    """
    sl.write(content)
    sl.write(comment)