import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime


st.title("Workout App")

today = datetime.today().strftime('%Y-%m-%d')



conn = sqlite3.connect('existingDB.db')


#@st.cache_data
lifts = pd.DataFrame(columns = ["Lift", "Weight", "Reps", "Date"])
st.table(lifts)

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
        #lifts.loc(len(lifts)) = [lift, weight, reps, today]








