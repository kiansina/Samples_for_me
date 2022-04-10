#find longitudes and latitudes
from functools import partial
from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent="googleearth")
geocode=partial(geolocator.geocode,language="en")
location=geolocator.geocode("175 5th avenue NYC")
print(location.latitude,location.longitude)
