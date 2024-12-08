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


st.header("5/3/1 Lifts")




new_x = st.button("Change Exercises or Maxes")

if new_x:
    with st.form("exercise_form"):
        st.write("Select exercises")
        vp = st.text_input("Input shoulder exercise")
        if vp:
            vp_max = st.text_input("Max")
        hinge = st.text_input("Hip hinge exercise")
        if hinge:
            hinge_max = st.text_input("Max")
        hp = st.text_input("Horizontal Press")
        if hp:
            hp_max = st.text_input("Max")
        leg = st.text_input("Leg Exercise")
        if leg:
            leg_max = st.text_input("Max")
        submitted = st.form_submit_button("Submit selections")
        if submitted:
            st.write("Selections locked in")










