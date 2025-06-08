import streamlit as st
import datetime
import pandas as pd

# Store workouts and results in session state
if 'workouts' not in st.session_state:
    st.session_state.workouts = {}

st.title("Workout Calendar")
st.write("Select a date below to view or add a workout for that day.")

# Use st.date_input for interactive calendar
selected_date = st.date_input("Select a date", value=st.session_state.get("selected_date", datetime.date.today()))
st.session_state.selected_date = selected_date

# Always show the form for the selected date
workout = st.session_state.workouts.get(
    str(selected_date),
    {"workout": "", "result": "", "mileage": "", "pace": ""}
)

st.subheader(f"Workout for {selected_date}")

# Use unique keys for each input to force Streamlit to refresh the form when the date changes
workout_desc = st.text_input(
    "Workout description",
    value=workout["workout"],
    key=f"workout_desc_{selected_date}"
)
mileage = st.text_input(
    "Mileage (miles)",
    value=workout.get("mileage", ""),
    key=f"mileage_{selected_date}"
)
pace = st.text_input(
    "Average pace (min/mile)",
    value=workout.get("pace", ""),
    key=f"pace_{selected_date}"
)

if selected_date < datetime.date.today():
    result = st.text_area(
        "How did the workout go?",
        value=workout["result"],
        key=f"result_{selected_date}"
    )
else:
    result = workout["result"]

if st.button("Save", key=f"save_{selected_date}"):
    st.session_state.workouts[str(selected_date)] = {
        "workout": workout_desc,
        "result": result,
        "mileage": mileage,
        "pace": pace
    }
    st.success("Workout saved!")

# Optionally, show a summary of all workouts
with st.expander("View all workouts"):
    for date, data in sorted(st.session_state.workouts.items()):
        st.write(
            f"**{date}**: {data['workout']} | Mileage: {data.get('mileage', '')} | Pace: {data.get('pace', '')} | Result: {data['result']}"
        )

# --- Weekly/Monthly Analytics ---

def parse_pace(pace_str):
    """Convert 'mm:ss' or float string to minutes as float."""
    if not pace_str or pace_str == "0":
        return 0.0
    try:
        # Try float conversion first
        return float(pace_str)
    except ValueError:
        try:
            # Try mm:ss format
            parts = pace_str.split(":")
            if len(parts) == 2:
                minutes = int(parts[0])
                seconds = int(parts[1])
                return minutes + seconds / 60.0
        except Exception:
            pass
    return 0.0

def format_pace(pace_float):
    """Format pace as mm:ss from float minutes."""
    if pace_float and pace_float > 0:
        minutes = int(pace_float)
        seconds = int(round((pace_float - minutes) * 60))
        return f"{minutes}:{seconds:02d} min/mile"
    return "N/A"

# Prepare DataFrame from workouts
df = pd.DataFrame([
    {
        "date": date,
        "mileage": float(data.get("mileage", 0) or 0),
        "pace": parse_pace(data.get("pace", 0))
    }
    for date, data in st.session_state.workouts.items()
])
if not df.empty:
    df["date"] = pd.to_datetime(df["date"])

    # Weekly analytics
    week = df[df["date"] >= (pd.Timestamp.today() - pd.Timedelta(days=7))]
    week_workouts = len(week)
    week_mileage = week["mileage"].sum()
    week_avg_pace = week["pace"][week["pace"] > 0].mean()

    # Monthly analytics
    month = df[df["date"] >= (pd.Timestamp.today() - pd.Timedelta(days=30))]
    month_workouts = len(month)
    month_mileage = month["mileage"].sum()
    month_avg_pace = month["pace"][month["pace"] > 0].mean()

    st.markdown("### Weekly Analytics")
    st.write(f"Total workouts: **{week_workouts}**")
    st.write(f"Total mileage: **{week_mileage:.2f}**")
    st.write(f"Average pace: **{format_pace(week_avg_pace)}**")

    st.markdown("### Monthly Analytics")
    st.write(f"Total workouts: **{month_workouts}**")
    st.write(f"Total mileage: **{month_mileage:.2f}**")
    st.write(f"Average pace: **{format_pace(month_avg_pace)}**")
else:
    st.markdown("### Weekly Analytics")
    st.write("No data available.")
    st.markdown("### Monthly Analytics")
    st.write("No data available.")