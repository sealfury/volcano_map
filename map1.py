import folium
import pandas

data = pandas.read_csv("data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
stockholm = [59.33258, 18.0649]

map = folium.Map(location=stockholm, zoom_start=4, tiles="Stamen Watercolor")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="Interested in volcanoes?",
            icon=folium.Icon(
                color="red", icon_color="yellow", icon="fa-fire", prefix="fa"
            ),
        )
    )
map.add_child(fg)

map.save("Map1.html")