
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.basemap 
from mpl_toolkits.basemap import Basemap
import datetime
import matplotlib.colors

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

fecha = np.array([datetime.datetime(1900,01,01)+\
datetime.timedelta(hours = time[i]) for i in range(len(time))])

#se recorta lat y lon para el punto 1

lat1=np.where(lat==12.625)[0][0]
lon1=np.where(lon==278.375)[0][0]
#se recort la info (time, lat , lon)

VientoU=Uwind[:,lat1,lon1]
VientoV=Vwind[:,lat1,lon1]

VientoU=VientoU*-1

#ciclo anual punto 1 SAI

CicloAnual_Viento= np.zeros([12]) * np.NaN

Meses = np.array([fecha[i].month for i in range(len(fecha))])
for k in range(1,13):
    tmpp = np.where(Meses == k)[0]
   
    altura1_tmp= VientoU[tmpp]
    CicloAnual_Viento[k-1]= np.mean(altura1_tmp)

Fig= plt.figure()
plt.rcParams.update({'font.size':14})
plt.plot(CicloAnual_Viento,'-', color='skyblue',lw=3,label='Hs')
x_label = ['Año']
plt.title('Ciclo Anual Altura de Ola Significante', fontsize=24)
plt.xlabel('Mes',fontsize=18)
plt.ylabel('Hs(metros)',fontsize=18)
plt.legend(loc=0)
plt.show()

axes = plt.gca()
axes.set_xlim([0,11])
axes.set_ylim([0.9,2.0])
axes.set_xticks([0,1,2, 3, 4, 5, 6, 7,8, 9, 10 ,11]) #choose which x locations to have ticks
axes.set_xticklabels(['Ene','Feb','Mar','Abr','May','Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic' ]) 
plt.savefig('CicloAnualAltura1.png')

#ciclo anual con pandas

Waves=pd.Series(index=fecha, data=altura1)

WavesM=Waves.resample('M').mean()
WavesD=Waves.resample('D').mean()

WM=np.array(WavesM)
WM=WM[:-6]
WM=np.reshape(WM,(-1,12))
WMM=np.mean(WM,axis=0)
WMS=np.std(WM, axis=0)

plt.plot(WMM)


