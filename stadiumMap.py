#-----------------------------------------
#ukates
#Bellevue University
#stadiumMap.property
#
#purpose of this program is to practice
#the creation of interactive maps. Also,
#to learn more about the use of pandas for
#data manipulation
#
#9/14/2019
#------------------------------------------

import pandas
import folium
#read csv files
mlb = pandas.read_csv("MLB Stadiums.csv")
nfl = pandas.read_csv("NFL Stadium Locations.csv")

#create list for mlb stadium lat and lon coordinates and names
mlbLat = list(mlb["Latitude"])
mlbLon = list(mlb["Longitude"])
mlbName = list(mlb["Stadium Name"])
#create list for nfl stadium name, lat and lon coordinates
nflLat = list(nfl["latitude"])
nflLon = list(nfl["longitude"])
nflName = list(nfl["Team"])

#create base map from folium
map = folium.Map(location = [39.5, -98.35], zoom_start = 5, tiles = "Stamen Terrain")
#create MLB statdium feature group for layering
fgMlb = folium.FeatureGroup(name = "MLB Stadiums")
#loop through mlb lists
for lt, ln, nm in zip(mlbLat, mlbLon, mlbName):
    #create mlb stadium markers
    fgMlb.add_child(folium.Marker(location = [lt, ln], popup = str(nm), icon = folium.Icon(color = 'red')))
#NFL stadium feature group
fgNfl = folium.FeatureGroup(name = "NFL Stadiums")
#loop through nfl lists
for lt, ln, nm in zip(nflLat, nflLon, nflName):
    #create nfl stadium markers
    fgNfl.add_child(folium.Marker(location = [lt, ln], popup = str(nm), icon = folium.Icon(color = 'blue')))

map.add_child(fgMlb) #add mlb feature group to base map as child
map.add_child(fgNfl) #add nfl feature group to base map as child

map.add_child(folium.LayerControl()) # create layer selections on map

map.save("stadiumMap.html")# create and save map as stadiumMap.html
