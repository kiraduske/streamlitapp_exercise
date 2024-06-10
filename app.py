import streamlit as st
import requests
import json
import pandas as pd

# Setting the title and description of the app
st.title("Women and Men Currently in Space")
st.markdown("""
This application displays the current number of people in space as well as their names using data from the Open Notify API.
""")

# Fetching data from the API
response = requests.get("http://api.open-notify.org/astros.json")

# Checking if the response status is OK (200)
if response.status_code == 200:
    data = response.json()
    
    # Displaying the total number of people in space
    st.header(f"Total number of people in space: {data['number']}")
    
    # Display the names of the people in space
    st.subheader("Names of people currently in space:")
    for person in data['people']:
        st.write(person['name'])
else:
    st.error("Failed to fetch data from the API")

# Section for ISS location
st.markdown("---")
st.header("Current Location of the International Space Station (ISS)")

# Fetching current location of the ISS
iss_response = requests.get("http://api.open-notify.org/iss-now.json")

# Checking if the response status is OK (200)
if iss_response.status_code == 200:
    iss_data = iss_response.json()
    
    # Extracting latitude and longitude
    iss_position = iss_data['iss_position']
    latitude = float(iss_position['latitude'])
    longitude = float(iss_position['longitude'])
    
    # Displaying the ISS location
    st.subheader("Current ISS Location")
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")
    
    # Creating a dataframe with the ISS position
    iss_df = pd.DataFrame({
        'lat': [latitude],
        'lon': [longitude]
    })
    
    # Display the map
    st.subheader("Geographical Map of Current ISS Location")
    st.map(iss_df)
    
    # Description for the map
    st.markdown("""
    The interactive map shows the current location of the International Space Station (ISS) in real-time.
    """)
else:
    st.error("Failed to fetch the ISS location data")