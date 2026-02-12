import json
import pandas as pd
import streamlit as st

with open("users.json", "r") as file:
    users = json.load(file)

st.header("Manage Users :material/people:")

df = pd.DataFrame(users).T.reset_index()
df.columns = ["Username","Password","Role"]
st.table(df[["Username","Role"]])