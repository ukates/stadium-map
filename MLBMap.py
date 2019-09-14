import pandas
import folium

mlb = pandas.read_csv("MLB Stadiums.csv")
nfl = pandas.read_csv("NFL Stadium Locations.csv")

mlbLat = list(mlb["Latitude"])
mlbLon = list(mlb["Longitude"])
mlbName = list(mlb["Stadium Name"])

nflLat = list(nfl["latitude"])
nflLon = list(nfl["longitude"])
nflName = list(nfl["Team"])


map = folium.Map(location = [39.5, -98.35], zoom_start = 5, tiles = "Stamen Terrain")

fgMlb = folium.FeatureGroup(name = "MLB Stadiums")

for lt, ln, nm in zip(mlbLat, mlbLon, mlbName):
    fgMlb.add_child(folium.Marker(location = [lt, ln], popup = str(nm), icon = folium.Icon(color = 'red')))

fgNfl = folium.FeatureGroup(name = "NFL Stadiums")

for lt, ln, nm in zip(nflLat, nflLon, nflName):
    fgNfl.add_child(folium.Marker(location = [lt, ln], popup = str(nm), icon = folium.Icon(color = 'blue')))

map.add_child(fgMlb)
map.add_child(fgNfl)

map.add_child(folium.LayerControl())

map.save("mlbmap.html")
