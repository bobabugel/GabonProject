# GabonProject

## Goal 
The goal of this project is to use 

## Data 
The data for this project comes for the 2016 NASA, ESA, Gabonese Space Agency mission call AfriSAR. The mission used , NASA UAVSAR(https://uavsar.jpl.nasa.gov/) and LVIS(https://lvis.gsfc.nasa.gov/Home/index.html) instruments collected data that will be used to derive forest canopy height, structure, and topography. This mission was a percuresr for NASA GEDI(https://gedi.umd.edu/) Mission and ESA BIOMASS Mission. 

### Study Sites 

This study site for this Project is Modah. This study site had ground measurements that were taken of of trees in 14 1 ha theat were they subseted into .625ha plot and .25ha plots. With in those plot all of the trees were measured for basal area, aboveground biomass, number of trees, maximum tree height, and basal-area-weighted wood specific gravity that were derived from (2) observations of nearly 6,700 individual trees including tree family, species, DBH, the height of each tree, and their x,y location within 25 x 25 m subplots. 

The Mondah study site (0.57° N, 9.35° E) is located ca. 25 km Northwest of Libreville toward Cap Esterias. Altitude seldom exceeds 50 m asl in this coastal area where mean temperature is 25 °C and mean annual rainfall falls within the range 3000–3500 mm, with a dry season occurring in June–September. The sandy-clayey soils in the area developed from shales and slates. Different vegetation types occur in this forested area, including Aucoumea-dominated forests and mixed forests. Some zones of the Mondah study area have undergone significant disturbance , but other patches remain protected . Mean tree species richness is similar to that in Lope, with high variations from one plot to ´ the other depending on disturbance level.

(https://daac.ornl.gov/AFRISAR/guides/AfriSAR_Mondah_Field_Data.html)

#### Trees 
For each 0.0625 ha subplot the data covers: GPS location of the 4 corners, x,y location of trees within a subplot, measurements of live tree family, species, DBH, height of each tree, and biomass at individual tree and plot level.  Data file: Mondah_Field_Data_Trees.csv.   Family and species of each tree was determined by a local botanist. DBH is the Diameter at Breast Height measured with a diameter measurement tape at 1.3 m height. Tree height measured in the field with DBH meter and a clinometer. Biomass of each tree is estimated using the Chave et al. 2014 equation with tree diameter, wood specific gravity (defined by tree species) and tree height. From the biomass of each individual tree, the biomass at plot level was calculated by adding the biomass of every tree within the 1 ha plot boundaries.

#### Plots 
At each plot level we calculated basal area, aboveground biomass, number of trees per plot, maximum tree height, and basal-area-weighted wood specific gravity.  Respective aggregated data files:  Mondah_Field_Data_Plot-0.0625ha.csv, Mondah_Field_Data_Plot-0.25ha.csv, and Mondah_Field_Data_Plot-1ha.csv. Biomass density information for different plot sizes was calculated by adding the biomass data for each individual tree within the boundaries of a certain subplot and divide by the area of that subplot to calculate biomass density for each subplot.

#### Flight Paths 
In Feb-Mar, 2016, LVIS was mounted in the Langley King Air and flown over selected sites in Gabon, Africa, as part of the joint NASA/ESA/DLR/AGEOS Afrisar Campaign. Data are available from 7 flights, in both Level1B and Level2 formats. The Level1b data files contain the geolocated laser waveform data for each laser footprint. The Level2 data files contain canopy top and ground elevations and relative heights derived from the Level1b data.
DATA  
(https://lvis.gsfc.nasa.gov/Data/Maps/Gabon2016Map.html)  
Work Flow   
(https://github.com/bobabugel/GabonProject/blob/master/Flight%20Path%20DATA%20.ipynb)  

## Method 

### Finding Study Site
For a site to be in this project the site must have a fall into a plot. Those plot need to have trees and LVIS data. 

### Looking at Lidar Returns from LEVEL 2 DATA 
This uses data from the L2 prouduct to look at RH data by plot. 
*Exploring LiDAR–RaDAR synergy—predicting aboveground biomass in a southwestern ponderosa pine forest using LiDAR, SAR and InSAR*  
**First Plot Created**  
https://github.com/bobabugel/GabonProject/blob/master/AGB5_AGBgraphedwithRH25_100.ipynb  
**Looking At RH & AGB by Shot**  
The chart here take the sum of the AGB from each tree in the shot and add them to get there sum. That sum is then ploted against the RH value from from each shot. 
https://github.com/bobabugel/GabonProject/blob/master/Finding_ABG5_Find_AGB_perShotnumber.ipynb

**Looking At RH & AGB by Plot**

**Looking At RH & AGB by Subplot .625**

**Looking At RH & AGB by Subplot.25 **

### Looking at Wavefroms 
This data set looks at The L1 beam to look at the above ground RH returns. 

**45612**  
https://github.com/bobabugel/GabonProject/blob/master/Finding_ABG6_H5py-h5_45612.ipynb  
**46644**  
(https://github.com/bobabugel/GabonProject/blob/master/Finding_ABG6_H5py-h5_46644.ipynb)  
  
### Using Wavefroms To find Biomass Index 
