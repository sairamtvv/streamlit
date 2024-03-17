import os


import pandas as pd
import plotly.graph_objs as go
import streamlit as st


import datetime
# from datetime import datetime

def connection_to_db(username):
    con =2
    return con
def main():
    plant = st.radio(
        "Choose plant or site",
        [":rainbow[Karnal]", ":rainbow[Biwadi]", "Hissar"],
        index=None,
        #captions=["Laugh out loud.", "Get the popcorn.", "Never stop learning."]
    )

    st.write("You selected:", plant)

    if plant == "Karnal":
        num_lst = list(range(1, 21))

        inverter_lst = list(map(lambda x: "inv-" + str(x), num_lst))

    elif plant == "Biwadi":
        num_lst = list(range(1, 15))

        inverter_lst = list(map(lambda x: "inv-" + str(x), num_lst))
    elif plant == "Hissar":
        num_lst = list(range(1, 5))

        inverter_lst = list(map(lambda x: "inv-" + str(x), num_lst))
    else:
        inverter_lst = []

    start_date = st.date_input(
        "Enter the start date:", datetime.date(2022, 3, 1)
    )

    end_date = st.date_input(
        "Enter the end date:", datetime.date(2023, 3, 1)
    )






    try:
        if plant is None:
            st.write("plant not selected  Please select plant id ")

        elif start_date == "":
            st.write("Please Enter a Start Date !")
        elif end_date == "":
            st.write("Please Enter End Date !")

        else:

            os.write(1, f" before _ start_date = {start_date}\n".encode())
            # Convert to datetime object
            date_obj = datetime.datetime.strptime(str(start_date), "%Y-%m-%d")
            # Format the date
            start_date = date_obj.strftime("%d.%m.%Y")
            # start_date =str(datetime.date.strptime(str(start_date), "%Y-%m-%d").strftime("%dd.%mm.%YYYY"))
            os.write(1, f" after start_date = {start_date}\n".encode())

            os.write(1, f" before _ end_date = {end_date}\n".encode())
            # Convert to datetime object
            date_obj = datetime.datetime.strptime(str(end_date), "%Y-%m-%d")
            # Format the date
            end_date = date_obj.strftime("%d.%m.%Y")
            # start_date =str(datetime.date.strptime(str(start_date), "%Y-%m-%d").strftime("%dd.%mm.%YYYY"))
            os.write(1, f" after start_date = {end_date}\n".encode())

    except Exception as e:
        st.warning(f"plant data not found: {e}")
