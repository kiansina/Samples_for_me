#finding the address and giving the coordinates
import pandas as pd
from functools import partial
from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent="googleearth")
geocode=partial(geolocator.geocode,language="en")
df = pd.read_excel(r'C:\Users\sina\Desktop\gioa.xlsx')
Address=list(df['FloodLocationName'])
result=[]
for i in Address:
    location=geolocator.geocode(i)  #location=geolocator.geocode(i,timeout=10)
    if location is None:
        result.append((None,None))
    else:
        result.append((location.latitude,location.longitude))

df["result"]=result
file_name='victory2.xlsx'
df.to_excel(file_name)
