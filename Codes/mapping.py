import folium
import webbrowser
import os
import csv
import pandas as pd
from folium.plugins import MarkerCluster
import numpy as np


myMap = folium.Map(location=[7.046581, 16.100688], zoom_start= 4)

with open('Algeria.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Algeria</strong>", tooltip= "Algeria", icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap)

with open('Angola.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Angola', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap)    
  
  
with open('botswana.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Botswana', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('burkinafaso.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Burkina Faso', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('burundi.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Burundi', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('caboverde.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Cabo Verde', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('cameroon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Cameroon', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('centralafricanrepublic.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Central African Republic', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('chad.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Chad', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('Comoros.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Comoros', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('congodemogrepublic.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Congo Democratic Republic', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('congorepublic.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Congo Republic', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('cotedivoire.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Cote dIvoire', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('egypt.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Egypt', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('ethiopia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Ethiopia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('gabon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Gabon', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('Gambia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Gambia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('ghana.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Ghana', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('guinea.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Guinea', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('guineabiss.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Guinea Bissau', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('kenya.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Kenya', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('lesotho.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Lesotho', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('liberia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Liberia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('libya.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Libya', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('madagascar.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Madagascar', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('malawi.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Malawi', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('mali.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Mali', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('mauiritius.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Mauiritius', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('mauritania.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Mauritania', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('morocco.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Morocco', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('mozambique.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Mozambique', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('namibia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Namibia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('niger.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Niger', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('nigeria.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Nigeria', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('rwanda.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Rwanda', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('saotome.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Sao Tome and Principe', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('senegal.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Senegal', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('seychelles.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Seychelles', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('sierraleone.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Sierra Leone', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('somalia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Somalia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('southafrica.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='South Africa', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('southsudan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='South Sudan', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('sudan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Sudan', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('tanzania.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Tanzania', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('togo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Togo', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('tunisia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Tunisia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('uganda.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Uganda', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('zambia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Zambia', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 

with open('zimbabwe.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Zimbabwe', icon=folium.Icon(color='blue', icon='ok-sign')).add_to(myMap) 



url2 = 'https://raw.githubusercontent.com/johan/world.geo.json/master'
state_geo = f'{url2}/countries.geo.json' #coordinat
africa_countries = 'africa.csv' #values with id 
state_data = pd.read_csv(africa_countries)



folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['id', 'NumberOf5StarHotels'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=5,
    legend_name='NumberOf5StarHotels'
).add_to(myMap)



myMap.save("myMap.html")





















myMap.save("myMap.html")