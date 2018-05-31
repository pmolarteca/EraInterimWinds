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
             
   

###promedio de vientos Mayos multianual#######################con fecha de Mayo2004


fechasrange=pd.date_range(start='1979/1/1', end='2017/12/31/18',freq='6H')

Mayos=np.where(fechasrange.month==5)[0]

fechasMayo=pd.date_range(start='2017/05/1', end='2017/05/31/18',freq='6H')
fechas_Mayo= np.array([fechasMayo[i].strftime('%Y%m%d %H%M%S') for i in range(len(fechasMayo))])



MediaMM=np.zeros([124,8,8])*np.NaN
DatosMayo=Vwind[Mayos]
for j in range(len(latnew)):
	for k in range (len(lonnew)):
		mediaM=np.reshape(DatosMayo[:,j,k],(39,124))
		MediaMM[:,j,k]=np.mean(mediaM,axis=0)
	

MediaMMU=np.zeros([124,8,8])*np.NaN
DatosMayo=Uwind[Mayos]
for j in range(len(latnew)):
	for k in range (len(lonnew)):
		mediaM=np.reshape(DatosMayo[:,j,k],(39,124))
		MediaMMU[:,j,k]=np.mean(mediaM,axis=0)




for i in (range(len(MediaMM))):
    with open('WIND_Mayos__2004.wind','a') as f:
        f.write(fechas[fecha1:fecha2+1][i]+"\n")
        for k in range (len(latnew)):
            line = "%s%s" % ('    ', "    ".join(map(str,(MediaMMU[i][k]))))
            f.write(line+"\n")
            if k==len(latnew)-1:
                 for j in range (len(latnew)):
                     line2 = "%s%s" % ('    ', "    ".join(map(str,(MediaMM[i][j]))))
                     f.write(line2+"\n")
             
   











