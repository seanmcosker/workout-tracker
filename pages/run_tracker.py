import streamlit as st
import datetime

# Store workouts and results in session state
if 'workouts' not in st.session_state:
    st.session_state.workouts = {}

st.title("Workout Calendar")

# Select a date from a calendar
selected_date = st.date_input("Select a date", datetime.date.today())

# Display workout for the selected date
workout = st.session_state.workouts.get(str(selected_date), {"workout": "", "result": ""})

st.subheader(f"Workout for {selected_date}")

# Input or view workout details
workout_desc = st.text_input("Workout description", value=workout["workout"], key=f"workout_{selected_date}")

# If the date is in the past, allow input of workout result
if selected_date < datetime.date.today():
    result = st.text_area("How did the workout go?", value=workout["result"], key=f"result_{selected_date}")
else:
    result = workout["result"]

# Save button
if st.button("Save", key=f"save_{selected_date}"):
    st.session_state.workouts[str(selected_date)] = {
        "workout": workout_desc,
        "result": result
    }
    st.success("Workout saved!")

# Optionally, show a summary of all workouts
with st.expander("View all workouts"):
    for date, data in sorted(st.session_state.workouts.items()):
        st.write(f"**{date}**: {data['workout']} - {data['result']}")