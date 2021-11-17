import folium
import pandas as pd 
import numpy as np
from datascience import *
import json
import geopandas as gpd

joined_df = pd.read_csv("state_mappings.csv")
states_locations = pd.read_csv("../data/State Locations.csv")

folium.Choropleth(
    geo_data=joined_df,
    data=joined_df,
    columns=['State/UT', "Rate of Total Crime Against Women (2019)"],
    key_on="feature.properties.NAME_1",
    fill_color='YlGnBu',
    fill_opacity=0.8,
    line_opacity=0.2,
    legend_name="total crime (2019)",
    smooth_factor=0,
    line_color = "#0000",
    nan_fill_color = "White"
).add_to(india_map)

states_arr = ['Andaman and Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh','Uttaranchal', 'West Bengal']

for i in np.arange(len(states_locations)):
    folium.Marker(location=[states_locations['Latitude (N)'][i], states_locations['Longitude (E)'][i]], popup=states_arr[i]).add_to(india_map)
    
india_map