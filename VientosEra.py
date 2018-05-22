# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 14:08:00 2018

@author: Unalmed
"""



from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.basemap 
from mpl_toolkits.basemap import Basemap
import datetime
import matplotlib.colors
import pandas as pd
from scipy import stats
import scipy.stats as scp

Data=Dataset('DataEraInterim_Wind.nc','r')
print Data.variables.keys()

U = np.array (Data.variables['u10'][:])
V = np.array (Data.variables['v10'][:])
lat = np.array (Data.variables['latitude'][:])
lon = np.array (Data.variables['longitude'][:])
time = np.array (Data.variables['time'][:])
time = time.astype(float)



fechas = []
for i in range(len(time)):
#print i
#print time[i]
    fechas.append(datetime.datetime(1900,01,01)+datetime.timedelta(hours = time[i]))

fechas = np.array(fechas)
print fechas



latnew=np.where((lat>=12.125) & (lat<=13))[0]

lonnew=np.where((lon>=360-82.125) & (lon<=360-81.25))[0]

Uwind=U[:,latnew,:]
Uwind=Uwind[:,:,lonnew]


Vwind=V[:,latnew,:]
Vwind=Vwind[:,:,lonnew]

#punto_bin = open('C:/Users/Unalmed/Documents/DatosSatelite/vientos.bin', 'wb')
#pickle.dump(Vwind[0], punto_bin)

#punto_bin = open('C:/Users/Unalmed/Documents/DatosSatelite/vientos.bin', 'wb')
#pickle.dump(Vwind[0], punto_bin)

#punto = open('C:/Users/Unalmed/Documents/DatosSatelite/vientos.bin','rb')
#VV = pickle.load(punto)


fechas= np.array([fechas[i].strftime('%Y%m%d %H%M%S') for i in range(len(fechas))])


fecha1=np.where(fechas=='20040101 000000')[0][0]
fecha2=np.where(fechas=='20040131 180000')[0][0]






for i in (range(fecha1,fecha2+1)):
    with open('WIND_testrun2.wind','a') as f:
        f.write(fechas[i]+"\n")
        for k in range (len(latnew)):
            line = "%s%s" % ('    ', "    ".join(map(str,(Uwind[i][k]))))
            f.write(line+"\n")
            if k==len(latnew)-1:
                 for j in range (len(latnew)):
                     line2 = "%s%s" % ('    ', "    ".join(map(str,(Vwind[i][j]))))
                     f.write(line2+"\n")
             
   
 
