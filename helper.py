import pandas as pd 
import streamlit as st 
import plotly.express as px 
import plotly.graph_objects as go 
import airportsdata 
import pycountry 
airports = airportsdata.load('IATA') 
st.set_page_config(layout='wide') 
st.title(':orange[fly]:blue[dubai]')
iata_code = st.text_input("Please enter the IATA code: ",max_chars=3).upper()
print(iata_code)
if st.button("Process: "):
    print(airports[iata_code])
    st.markdown("**ICAO Code:** "+airports[iata_code]['icao'])
    st.markdown("**Airport Name:** "+airports[iata_code]['name'])
    st.markdown("**City:** "+airports[iata_code]['city'])
    st.markdown("**Subdivision:** "+airports[iata_code]['subd'])
    st.markdown("**Country Code ISO-2:** "+airports[iata_code]['country'])
    #getting the ISO-3 country code 
    var = pycountry.countries.get(alpha_2=airports[iata_code]['country'])
    st.markdown("**Country Code ISO-3:** "+pycountry.countries.get(alpha_2=airports[iata_code]['country']).alpha_3)
