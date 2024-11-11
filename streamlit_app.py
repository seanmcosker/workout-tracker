import streamlit as st
import pandas as pd
import sqlite3

st.title("Workout App")
conn = sqlite3.connect('existingDB.db')

st.table()

with st.form("input_form"):
    st.write("Log today's top set")
    lift = st.selectbox('Select exercise', 
             ["OHP", "Bench", "Squat", "Deadlift"])
    weight = st.text_input("Weight")
    reps = st.text_input("Reps")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Lift", lift, "weight", weight, "Reps", reps)
        







