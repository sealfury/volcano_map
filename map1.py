import folium
import pandas

stockholm = [59.33258, 18.0649]
data = pandas.read_csv("data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano Information:</h4>
Height: %s m 
"""


def colorize(elevation):
    if elevation < 1200:
        return "green"
    elif elevation > 2800:
        return "red"
    else:
        return "orange"


map = folium.Map(location=stockholm, zoom_start=4, tiles="Stamen Watercolor")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Icon(color=colorize(el), icon="fa-fire", prefix="fa"),
        )
    )

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open("data/world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda s: {
            "fillColor": "#b69cff"
            if s["properties"]["POP2005"] < 10000000
            else "#98faaa"
            if s["properties"]["POP2005"] >= 50000000
            else "#ff455e"
        },
    )
)

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")