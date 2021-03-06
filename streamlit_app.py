import pandas as pd
from datetime import datetime
import plotly.express as px
import numpy as np
import streamlit as st

# Using plotly.express
import plotly.express as px
import re

st.set_page_config(layout="wide")

data = pd.read_csv("data/merged_file_v4.xlsx - STEP 2 - Title.csv")
data = data[
    ["Institution_Name", "Institution_School", "Course_Name", "Course_Level(ii)"]
]

elements = st.text_area(
    "write query for using. For now you must use 'OR' for keys and the app searches everythings that contains with ignorecase",
    placeholder="biociências OR medicina",
)

strings = "|(\A|\W+)".join(elements.split(" OR "))
strings += "(\A|\W+)" + strings
print(strings)
query = re.compile(
    strings,
    re.IGNORECASE,
)

if strings:
    ncol1, ncol2 = st.columns(2)
    ncol1.markdown("Included courses")
    inc = data[data["Course_Name"].str.contains(query)]
    ncol2.metric("Rows", len(inc))
    st.dataframe(data=inc)

    mcol1, mcol2 = st.columns(2)
    mcol1.markdown("Exccluded courses")
    exc = data[~data["Course_Name"].str.contains(query)]
    mcol2.metric("Rows", len(exc))
    st.dataframe(data=exc)
