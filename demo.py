import pandas as pd
import streamlit as st

st.title("Practice")

DATA_PATH = "storm.csv"


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_PATH, nrows=nrows)

    def lowercase(x):
        return str(x).lower()

    data.rename(lowercase, axis="columns", inplace=True)
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text("Loading data...")
# Load 10,000 rows of data into the dataframe.
data = load_data(50000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")


st.subheader("Raw data")
st.write(data)

st.subheader("Map")
st.map(data)
