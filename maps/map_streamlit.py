
import folium
import streamlit as st

from streamlit_folium import st_folium

coord = (52.515, 13.35)
berlin = folium.Map(location=coord, zoom_start=14)

folium.Marker(
    (52.5158645, 13.3773881),
    popup="Brandenburger Tor",
    icon=folium.Icon(icon="map-marker", color="blue"),
).add_to(berlin)

folium.Marker(
    (52.5129613, 13.3487917),
    popup="Siegesäule",
    icon=folium.Icon(icon="map-marker", color="blue"),
).add_to(berlin)

#berlin.save("berlin.html")
st_data = st_folium(berlin, width=725)
st.write("done")
