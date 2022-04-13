import streamlit as st
import pandas as pd
import numpy as np

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment_counter():
	st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)

file = pd.read_csv("/Users/williamchan/Documents/AppliedML/baseballdatabank/core/Batting.csv")

df = file[["H","R"]]

st.line_chart(df)
