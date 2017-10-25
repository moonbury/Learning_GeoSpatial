import folium
import urllib2

path = urllib2.urlopen("https://api.myjson.com/bins/467pm")


m = folium.Map()
#m.geo_json(geo_path="https://api.myjson.com/bins/467pm")
folium.GeoJson(open("location.json")).add_to(m)

m.create_map(path="map.html")