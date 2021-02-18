import folium
import pandas

data = pandas.read_csv("data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
stockholm = [59.33258, 18.0649]

html = """<h4>Volcano Information:</h4>
Height: %s m 
"""

map = folium.Map(location=stockholm, zoom_start=4, tiles="Stamen Watercolor")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Icon(
                color="red", icon_color="yellow", icon="fa-fire", prefix="fa"
            ),
        )
    )
map.add_child(fg)

map.save("Map1.html")