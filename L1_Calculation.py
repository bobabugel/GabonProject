#Libs
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd
import h5py
import geopandas as gpd
from shapely.geometry import *
from geopandas.geoseries import *
import sys
from scipy.interpolate import make_interp_spline, BSpline
from scipy import misc
from scipy.ndimage import gaussian_filter

##Import
#L2 is the processed product
L2 =pd.read_csv(r'D:\Gabon_Lidar\DATA\LEVEL2_0308\csv\LVIS2_Gabon2016_0308_R1808_045612.csv')

#L1 is the waveform product- the 'r' is for reading
lvis = h5py.File(r'D:\Gabon_Lidar\DATA\LEVEL1_0308\LVIS1B_Gabon2016_0308_R1808_045612.h5','r')


#Reading get wave index from shotnumber and test if exists
all_shotnums = np.array(lvis['SHOTNUMBER'])
wave_idx = ''
Zmax = ''
wfrange = 1024
wfsize = 1023


#Create ShotNumber
SHOTNUMBER = lvis.get('SHOTNUMBER')
SHOTNUMBER_arr= np.array(SHOTNUMBER)
SHOTNUMBER_df = pd.DataFrame(SHOTNUMBER_arr,
             columns=['SHOTNUMBER'])

SHOTNUMBER_df.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\SHOTNUMBER_df.csv')
SHOTNUMBER_df =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\SHOTNUMBER_df.csv')
SHOTNUMBER_df.columns = ['index', 'SHOTNUMBER']


#Create Z0
Z0 = lvis.get('Z0')
Z0_arr = np.array(Z0)
Z0_df = pd.DataFrame(Z0_arr,
             columns=['ZO'])

Z0_df.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\Z0_df.csv')
Z0_df =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\Z0_df.csv')
Z0_df.columns = ['index', 'ZO']
SHOTNUMBER_Z0_df = SHOTNUMBER_df.set_index('index').join(Z0_df.set_index('index'))

#Create Z1023
Z1023 = lvis.get('Z1023')
Z1023_arr = np.array(Z1023)
Z1023_df = pd.DataFrame(Z0_arr,
             columns=['Z1023'])

Z1023_df.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\Z1023_df.csv')
Z1023_df =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\Z1023_df.csv')
Z1023_df.columns = ['index', 'Z1023']

SHOTNUMBER_Z1023_df = SHOTNUMBER_df.set_index('index').join(Z1023_df.set_index('index'))
print('DONE')
#Join to the L2 product

#L2
L2_Z1023 = L2.set_index('SHOTNUMBER').join(SHOTNUMBER_Z1023_df.set_index('SHOTNUMBER'))
L2_Z1023.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_Z1023.csv')
L2_Z1023 =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_Z1023.csv')

print('DONE')
L2_Z0 = L2_Z1023.set_index('SHOTNUMBER').join(SHOTNUMBER_Z0_df.set_index('SHOTNUMBER'))
print('DONE')
L2_Z0.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_Z0.csv')
L2_A =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_Z0.csv')

#Calculate heigth
L2_A['heigth'] = L2_A['ZO'] - L2_A['Z1023']

#Calculate zstrech
L2_A['zstretch'] =  L2_A['Z1023'] + (wfrange)*((L2_A['ZO'] - L2_A['Z1023'])/int(wfsize))


#extract the single waveform and elevation attributes Z0 and Z1023;
wave = np.array(lvis['RXWAVE'])



#Converting fields to Floats
#ZG = float(L2['ZG'])
#ZT = float(L2['ZT'])
#RH25 = float(L2['RH25'])
#RH50 = float(L2['RH50'])
#RH75 = float(L2['RH75'])
#RH10 = float(L2['RH10'])
#RH100 = float(L2['RH100'])

#Smooth
waveform = gaussian_filter(wave, sigma=3)

#set the z range limits for plotting the waveform to crop the noise  - This is for croping
L2_A['zmin']= L2_A['RH10']-(L2_A['ZT']-L2_A['RH10'])/6   #sets zmin at 15% below the waveform range defined in RH10-ZT

L2_A['zmax']= L2_A['ZT']+(L2_A['ZT']-L2_A['RH10'])/18   #sets zmax at 5% above the waveform range defined in RH10-ZT

#This subtract with the ground height normalizing everything
L2_A['zstretch_ground'] = L2_A['zstretch'] - L2_A['ZG']


L2_A.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_A.csv')
L2_A =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_A.csv')

#Import Waveform data
RXWAVE = lvis.get('RXWAVE').value
#turn into pandas DF
RXWAVE = pd.DataFrame(RXWAVE)

#Label RXWAVE by Shotnumber
RXWAVE = pd.concat([SHOTNUMBER_df,RXWAVE], axis=1, sort=False)

RXWAVE.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\RXWAVE.csv')
RXWAVE = pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\RXWAVE.csv')
RXWAVE = RXWAVE.drop('Unnamed: 0' , axis='columns')

#Join with LA
L2_RXWAVE = L2_A.set_index('SHOTNUMBER').join(RXWAVE.set_index('SHOTNUMBER'))

L2_RXWAVE.to_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_RXWAVE.csv')
L2_RXWAVE =pd.read_csv(r'D:\Gabon_Lidar\DATA\pandas_csv\L2_RXWAVE.csv')


#Good Above this
arr =  np.array(L2_RXWAVE['0'].values.tolist())

df1 = np.where(arr > L2_RXWAVE['zstretch_ground'], 0, arr).tolist()


filter = ((L2_RXWAVE.iloc[(:,51:1024)] )

#Create list
L2_RXWAVE = (L2_RXWAVE.iloc[(:,51:1024 > L2_RXWAVE['zstretch_ground'], '0' ])

filter = ((L2_RXWAVE.iloc[(:,51:1024)] > L2_RXWAVE['zstretch_ground'])

#Create list
L2_RXWAVE['zstretch_biomass'] = (L2_RXWAVE.iloc[:,51:1024].sum(axis =1) > L2_RXWAVE['zstretch_ground'])




L2_RXWAVE['zstretch_biomass'] = (L2_RXWAVE.iloc[:,51:1024].sum(axis =1) > 6)

L2_RXWAVE = L2_RXWAVEa.loc[(L2_RXWAVE.iloc[:,51:1024]< L2_RXWAVE['zstretch_ground'] ), ] = 0




#L2_RXWAVEa = (L2_RXWAVE.iloc[:,51:1024], L2_RXWAVE.iloc[:,51:1024] > L2_RXWAVE['zstretch_ground'])



filt = L2_RXWAVE.iloc[:,51:1024] >= L2_RXWAVE['zstretch_ground']



L2_RXWAVEa = (L2_RXWAVE.iloc[:,51:1024]  > L2_RXWAVE['zstretch_ground'])


L2_RXWAVEa = (L2_RXWAVE > L2_A['zstretch_ground'] )


#remove list
col_list    = col_list

L2_RXWAVE['zstretch_biomass'] = col_list.sum()

L2_RXWAVEa['zstretch_biomass'] = L2_RXWAVE[col_list].sum(min_count ='zstretch_ground')





['zstretch_ground'] = L2_A['zstretch'] - L2_A['ZG']
new_df = L2_RXWAVE.iloc[:,<51:1075].sum()

#Filtering the Arrau for ground and height





#The bumps the selected shot again the shot list
wave_idx = np.where(all_shotnums==int(myshotnum)[0][0]

#extract the single waveform and elevation attributes Z0 and Z1023;
waveform = lvis['RXWAVE'][wave_idx]

#This extracting the Z0
Z0 = int(lvis['Z0'][wave_idx])

#This extracting the Z1023
Z1023 = int(lvis['Z1023'][wave_idx])

#Check if this does anything
x = Z0 - Z1023

#This brings in the L2 Product
L2 = L2[(L2['SHOTNUMBER'] == myshotnum)]

#find the elevation difference from Z0 to Z1023 and divide into 1023 equal intervals
zstretch = np.add(Z1023,np.multiply(range(wfrange,0,-1),((Z0-Z1023)/int(wfsize))))

#Converting fields to Floats
ZG = float(L2['ZG'])
ZT = float(L2['ZT'])
RH25 = float(L2['RH25'])
RH50 = float(L2['RH50'])
RH75 = float(L2['RH75'])
RH10 = float(L2['RH10'])
RH100 = float(L2['RH100'])

#Smooth
waveform = gaussian_filter(waveform, sigma=3)

## Create Elevation Chart

#set the z range limits for plotting the waveform to crop the noise  - This is for croping
zmin=RH10-(ZT-RH10)/6   #sets zmin at 15% below the waveform range defined in RH10-ZT
zmax=ZT+(ZT-RH10)/18   #sets zmax at 5% above the waveform range defined in RH10-ZT

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

# set the z range limits for plotting the waveform to crop the noise
zmin = RH10 - (ZT - RH10) / 6  # sets zmin at 15% below the waveform range defined in RH10-ZT
zmax = ZT + (ZT - RH10) / 18  # sets zmax at 5% above the waveform range defined in RH10-ZT

#find the elevation difference from Z0 to Z1023 and divide into 1023 equal intervals
zstretch = np.add(Z1023,np.multiply(range(wfrange,0,-1),((Z0-Z1023)/int(wfsize))))

#This subtract with the ground height normalizing everything
zstretch = zstretch - ZG

#Filtering the Arrau for ground and height
filter = np.logical_and( RH10 < zstretch, zstretch <  RH100)

#Filter Zstrech for only those values that between
zstretch_filtered = zstretch[filter]

#Filter for waveform for only those that match with zstretch
waveform_filtered = waveform[filter]

zstretch_biomass  =sum ((zstretch_filtered**2) *waveform_filtered )