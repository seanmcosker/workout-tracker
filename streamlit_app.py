import streamlit as st
import pandas as pd
import sqlite3

st.title("Workout App")
conn = sqlite3.connect('existingDB.db')

st.table()

lift = st.selectbox('Select exercise', 
             ["OHP", "Bench", "Squat", "Deadlift"])