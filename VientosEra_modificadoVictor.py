## Entrada de vientos WWIII

#librerias
import numpy as np
import matplotlib as plt
import dateutil.rrule as rrule
import datetime as datetime
import pandas as pd

from netCDF4 import Dataset

Wind=Dataset('DataEraInterim_Wind.nc','r')
print Wind.variables
print Wind.variables.keys()

Uwind= np.array(Wind.variables['u10'][:])
Vwind= np.array(Wind.variables['v10'][:])
lat= np.array(Wind.variables['latitude'][:])
lon= np.array(Wind.variables['longitude'][:])
time= np.array(Wind.variables['time'][:]).astype(np.float)

Uwind[Uwind==-32767]=np.nan
Vwind[Vwind==-32767]=np.nan

latnew=np.where((lat>=12.125) & (lat<=13))[0]
lonnew=np.where((lon>=360-82.125) & (lon<=360-81.25))[0]
Uwind=U[:,latnew,:]
Uwind=Uwind[:,:,lonnew]
Vwind=V[:,latnew,:]
Vwind=Vwind[:,:,lonnew]

fecha = np.array([datetime.datetime(1900,01,01)+\
datetime.timedelta(hours = time[i]) for i in range(len(time))])

Lon, Lat = np.meshgrid(lon, lat)



fechas= np.array([fechas[i].strftime('%Y%m%d %H%M%S') for i in range(len(fechas))])

fecha1=np.where(fechas=='20040101 000000')[0][0]
fecha2=np.where(fechas=='20040131 180000')[0][0]




with open("WIND_test3.wind",
"w") as j:
    for i in range(fecha1,fecha2+1):
        j.write(fechas[i]+"\n")
        np.savetxt(j,np.vstack((Uwind[i,:,:],Vwind[i,:,:])),"%10.4f")  # (lon,Lat,time)
        #np.savetxt(j, u[i,:,:], "%10.4f")
        #np.savetxt(j, v[i,:,:], "%10.4f")

