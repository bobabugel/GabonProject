#Import Lib
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd
import h5py
import geopandas as gpd
from shapely.geometry import *
from geopandas.geoseries import *
import sys

#Import L2 Product
L2_045612 =(r'D:\Gabon_Lidar\DATA\LEVEL2_0308\LVIS2B_Gabon2016_0308_R1808_045612.txt')

#Import L1 Product
lvis = h5py.File(r'D:\Gabon_Lidar\DATA\LEVEL1_0308\LVIS1B_Gabon2016_0308_R1808_045612.h5','r')
#get wave index from shotnumber and test if exists
all_shotnums = np.array(lvis['SHOTNUMBER'])
wave_idx = ''
Zmax = ''
wfrange = 1024
wfsize = 1023

#Bring in Shot of intrest
#This looks Good
myshotnum = int(9361769)

#Looking for my shot in the array
wave_idx = np.where(all_shotnums==myshotnum)[0][0]

#extract the single waveform and elevation attributes Z0 and Z1023;
waveform = lvis['RXWAVE'][wave_idx]

Z0 = int(lvis['Z0'][wave_idx])

Z1023 = int(lvis['Z1023'][wave_idx])

x = Z0 - Z1023

L2 =pd.read_csv(r'D:\Gabon_Lidar\DATA\LEVEL2_0308\csv\LVIS2_Gabon2016_0308_R1808_045612.csv')

L2 = L2[(L2['SHOTNUMBER'] == myshotnum)]

#find the elevation difference from Z0 to Z1023 and divide into 1023 equal intervals
zstretch = np.add(Z1023,np.multiply(range(wfrange,0,-1),((Z0-Z1023)/int(wfsize))))

#ZG is ground return
ZG = float(L2['ZG'])

#ZG is top  return
ZT = float(L2['ZT'])

RH25 = float(L2['RH25']+L2['ZG'])

RH50 = float(L2['RH50']+L2['ZG'])

RH75 = float(L2['RH75']+L2['ZG'])

RH10 = float(L2['RH10']+L2['ZG'])

# set the z range limits for plotting the waveform to crop the noise
zmin = RH10 - (ZT - RH10) / 6  # sets zmin at 15% below the waveform range defined in RH10-ZT
zmax = ZT + (ZT - RH10) / 18  # sets zmax at 5% above the waveform range defined in RH10-ZT

# crop the waveform and elevation arrays to the z range limits
x = zstretch >= zmin  # this returns boolean True/False based on the comparison condition statement
y = zstretch <= zmax
z = (x == y)  # this creates a combined boolean result from the previous two condition statements
waveform_crop = []
zstretch_crop = []
for i in range(0, len(waveform)):
    if z[i] == True:
        waveform_crop.append(waveform[i])
        zstretch_crop.append(zstretch[i])

#plot the waveform as matplotlib figure
fig = plt.figure(figsize=(15, 6))
figplot = fig.add_subplot(121)
figplot.plot(waveform,zstretch)
plt.ylabel('elevation(m)')
plt.xlabel('amplitude')

figplot = fig.add_subplot(122)
figplot.plot(waveform_crop,zstretch_crop)
figplot.hlines(ZT,min(waveform),max(waveform),lw=1,linestyle='-', color='b',label='ZT')
figplot.hlines(RH75,min(waveform),max(waveform),lw=1,linestyle='-', color='g',label='RH75')
figplot.hlines(RH50,min(waveform),max(waveform),lw=1,linestyle='-', color='y',label='RH50')
figplot.hlines(RH25,min(waveform),max(waveform),lw=1,linestyle='-', color='orange',label='RH25')
figplot.hlines(ZG,min(waveform),max(waveform),lw=1,linestyle='-', color='r',label='ZG')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=5, mode="expand", borderaxespad=0.)
plt.ylabel('elevation(m)')
plt.xlabel('amplitude')
plt.show(block=False)

#This is my problem. I'm trying to shift the elevelation values to a hieght value

waveforma = np.subtract(waveform,ZG)

#waveforma = waveform.astype(np.int16)

waveforma

# plot the waveform as matplotlib figure
fig = plt.figure(figsize=(15, 6))
figplot = fig.add_subplot(121)
figplot.plot(waveforma, zstretch)
plt.ylabel('elevation(m)')
plt.xlabel('amplitude')

figplot = fig.add_subplot(122)
figplot.plot(waveform_crop, zstretch_crop)
figplot.hlines(ZT, min(waveforma), max(waveforma), lw=1, linestyle='-', color='b', label='ZT')
figplot.hlines(RH75, min(waveforma), max(waveforma), lw=1, linestyle='-', color='g', label='RH75')
figplot.hlines(RH50, min(waveforma), max(waveforma), lw=1, linestyle='-', color='y', label='RH50')
figplot.hlines(RH25, min(waveforma), max(waveforma), lw=1, linestyle='-', color='orange', label='RH25')
figplot.hlines(ZG, min(waveforma), max(waveforma), lw=1, linestyle='-', color='r', label='ZG')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=5, mode="expand", borderaxespad=0.)
plt.ylabel('elevation(m)')
plt.xlabel('amplitude')
plt.show(block=False)