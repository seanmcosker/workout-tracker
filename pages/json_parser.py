import streamlit as st

st.title("JSON Parser")
st.text("Parse those annyoing JSONs")

st.markdown("A bit of context: My inspiration for writing this tool came from my time working with AWS Bedrock APIs. A lot of those APIs returned JSONs with the field I wanted being 8-10 layers deep. Additionally, figured out the correct syntax to hit this JSON was tricky - hence I decided to biuld a tool to try and help")

my_json = st.text_input("Paste JSON here")
st.json(my_json)