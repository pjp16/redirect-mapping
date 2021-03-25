import streamlit as st
import pandas as pd

st.write('Number of Talks Watched')

st.write(pd.DataFrame({
    'Levi': [10],
    'Phill': [5],
    'Oli': [1]
}))

