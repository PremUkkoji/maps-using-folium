import folium
import pandas

volcanoes_data = pandas.read_csv("volcanoes.txt")
lat = list(volcaneos_data["LAT"])
lon = list(volcaneos_data["LON"])
elev = list(volcanoes_data["ELEV"])

def elev_color(el):
    if el <=2000:
        return "green"
    elif 2000 < el <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58, -110.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

for la, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [la, ln], radius=7, popup=folium.Popup(str(el)+" m", parse_html=True), fill_color=elev_color(el), fill=True, color="grey", fill_opacity=0.7))

file=open("world.json", "r", encoding="utf-8-sig")
fgp.add_child(folium.GeoJson(file.read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"]
 <= 10000000 else "orange" if 10000000 < x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

file.close()
map.save("web_map.html")
