##https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
import geopandas
import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
world.plot(cmap='OrRd')
ax = cities.plot(color='k')

world.plot(ax=ax);
#plt.show()
#############################################
import geopandas
import geoplot
import mapclassify

world = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)
fig, ax = plt.subplots(figsize = (10,4), facecolor = plt.cm.Blues(.2))
fig.suptitle('Country Populations',
             fontsize = 'xx-large',
             fontweight = 'bold')
ax.set_facecolor(plt.cm.Blues(.2))
world.plot(column = 'pop_est',
           cmap = 'Greens',
           ax = ax,
           legend = True)

#plt.show()
#############################################
fig, ax = plt.subplots(figsize = (6,5), facecolor = plt.cm.Blues(.2))
fig.suptitle('Africa Populations',
             fontsize = 'xx-large',
             fontweight = 'bold')
ax.set_facecolor(plt.cm.Blues(.2))
ax = world[world.continent == 'Africa'].plot(
    column = 'pop_est',
    cmap = 'Greens',
    ax = ax,
    legend = True)

plt.show()






############################################
