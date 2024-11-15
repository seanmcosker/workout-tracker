import streamlit as st
import pandas as pd
import os


st.title("Finance tracker")
#st.table()

DATA_FILE = "finance.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["TransactionID", "Amount", "Description", "Running Total", "Category"])

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def display_table(df):
    st.dataframe(df)

def add_data(df):
    with st.form("add_data_form"):
        tid = len(df)
        amt = st.number_input("Amount", step=0.01)
        desc = st.text_input("Description")
        category = st.selectbox(label = "Category", options = ["Food", "Clothes", "BJJ", "Games", "Cammy"])
        submitted = st.form_submit_button("Add Transaction")
        
        if submitted:
            new_data = pd.DataFrame({
                "TransactionID": [tid], #placeholder
                "Amount": [amt], 
                "Description": [desc],
                "Running Total": [0], #placeholder
                'Category': [category]})
            df = pd.concat([df, new_data], ignore_index=True)
            df["Running Total"] = df.Amount.cumsum()
            save_data(df)
            st.success("Transaction added successfully!")
            st.rerun()
    return df




df = load_data()
#st.text(len(df))
display_table(df)
df = add_data(df)


