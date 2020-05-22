import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = """Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a></br>
Height: %s m"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[39.8283, -98.5795], zoom_start=5, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volcanoes')
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width='220px', height='60px')
    fgv.add_child(folium.Marker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el)), opacity=0.7))
map.add_child(fgv)

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save('webmap.html')
