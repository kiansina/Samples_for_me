#finding the address and giving the coordinates
import pandas as pd
from functools import partial
from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent="googleearth")
geocode=partial(geolocator.geocode,language="en")
df = pd.read_excel(r'C:\Users\sina\Desktop\strategica\FacSimileUbicazioni.xlsx')
Address=list(df['Indirizzo completo'])
longlat=[]
for i in Address:
    location=geolocator.geocode(i)
    if location is None:
        longlat.append((None,None))
    else:
        longlat.append((location.latitude,location.longitude))

df["longlat"]=longlat
file_name='ResultStrategica.xlsx'
df.to_excel(file_name)
