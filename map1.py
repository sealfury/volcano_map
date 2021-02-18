import folium

rejk = [64.1477, -21.93274]
map = folium.Map(location=rejk, zoom_start=4, tiles="Stamen Watercolor")


map.add_child(
    folium.Marker(
        location=rejk, popup="Interested in volcanoes?", icon=folium.Icon(color="green")
    )
)

map.save("Map1.html")