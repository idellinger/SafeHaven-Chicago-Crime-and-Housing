import streamlit as st
from pickle import load
import folium
import streamlit_folium
import branca
import geopandas as gpd
st.title("Interactive Crime Map")

crime_neighborhood_merge_path = (r'C:\Data Science\chicago-crime-property-analysis\Israel\app\resources\data\crime_neighborhood_merge.geojson')
crime_neighborhood_merge = gpd.read_file(crime_neighborhood_merge_path)

crime_columns = ['Crimes Involving Children', 'Deceptive Practices and Fraud', 'Drug-Related Crimes',
                 'Property Crimes', 'Public Order Crimes', 'Violent Crimes']
crime_neighborhood_merge['total_crime'] = crime_neighborhood_merge.groupby('community')[crime_columns].transform('sum').sum(axis=1)

colormap = branca.colormap.LinearColormap(vmin=crime_neighborhood_merge['total_crime'].quantile(0.0),vmax=crime_neighborhood_merge['total_crime'].quantile(1),colors=["red", "orange", "lightblue", "green", "darkgreen"],caption="Total Crimes")

m = folium.Map(location=[41.84469250265398, -87.60914087617894], zoom_start=10)

popup = folium.GeoJsonPopup(
    fields=['community', 'Crimes Involving Children','Deceptive Practices and Fraud','Drug-Related Crimes','Property Crimes','Public Order Crimes','Violent Crimes'],
    aliases=['Neighborhood','Crimes Involving Children','Deceptive Practices and Fraud','Drug-Related Crimes','Property Crimes','Public Order Crimes','Violent Crimes'],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)

tooltip = folium.GeoJsonTooltip(
    fields=['community', 'Crimes Involving Children','Deceptive Practices and Fraud','Drug-Related Crimes','Property Crimes','Public Order Crimes','Violent Crimes'],
    aliases=['Neighborhood','Crimes Involving Children','Deceptive Practices and Fraud','Drug-Related Crimes','Property Crimes','Public Order Crimes','Violent Crimes'],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 1px solid black;
        border-radius: 2px;
        box-shadow: 2px;
    """,
    max_width=800,
)

g = folium.GeoJson(crime_neighborhood_merge,
                   style_function=lambda x: {"fillColor": colormap(x["properties"]["total_crime"])
                                             if x["properties"]["total_crime"] is not None
                                             else "transparent",
                                             "color": "black",
                                             "fillOpacity": 0.1},
                   tooltip=tooltip,
                   popup=popup).add_to(m)

colormap.add_to(m)


streamlit_folium.folium_static(m)

