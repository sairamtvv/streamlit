import streamlit as st
from pages.scripts import forecast_visualizer

st.set_page_config(page_title="Forecasts", layout="wide")

forecast_visualizer.main()
