# Abstract   
Introduction 

	Understanding aboveground biomass is important metric in understanding climate change and is an important part in calculating the amount of carbon that a forest sequesters (Ravindranath and Ostwald 2008). This the Reduce Emissions from Deforestation and forest Degradation (REDD) which is art of the United Nation Framework convention on Climate Change (UNFCCC) (Miles and Kapos 2008). This is extremely important ins tropical regions around the equator that are dealing with climate change and poverty (Chave , Rejou-Mechain, et al. 2015). Using direct measurements that include cutting down the tree are expensive and destructive  (Jenkins , et al. 2003). Even with using index like DRYAD (Zanne, et al. 2009) and ForC (Anderson-Teixeira, et al. 2018) analyzing AGB is difficult. The leads to the use of LiDAR and SAR to measure AGB. 
	This led to the 2016 AfriSAR NASA mission with collaboration with the European Space Agency (ESA) and the Gabonese Space Agency.  The mission included ground measurement, airborne based radar from NASA UAVSAR and airborne based LiDAR From LVIS at the time of the AFriSAR (Labriere, et al. 2018). In the following years spaceborne lidar in the form Global Ecosystem Dynamics Investigation (GEDI) (Dubayah, et al. 2020) has follow over the site. The goal of AfriSAR was to collaborate sensors for future spaceborne missions(Fatoyinbo, et al. 2017). With this there has been a push to created a global model to predict aboveground biomass around the world with one model (Knapp, et al. 2019). This is because historically many of the model are localized and over fit to one ecosystem. 
	NASA UAVSAR is a radar based system. SAR stands for synthetic aperture radar.  Radar base system use radio wave to look the tree canopy. For this project they used both L_Band and P-Band Data. In the AfriSAR study they were compared with LVIS lidar (Pardini, et al. 2018). The Band different length of radio waves. The P-band was operated with a 50 MHz bandwidth centered at 435 MHz (equivalent to a wavelength of 69 cm), while the L-band was operated with a 100 MHz bandwidth centered at 1.325 GHz (equivalent to a wavelength of 23 cm). The L-Band provides a great amount of vertical detail. 
	In other ecosystem LiDAR – RaDAR has had a synergy at predicting above ground biomass (Hyde, et al. 2007). With the advent of waveform lidar instead of just pulse wave lidar this mean the need for radar component can be reduced. The effectiveness in using just waveform is show in the northeastern united states (Ni-Meister, Yang, et al. 2017). This study uses proven methodology from New England on the tree data from the AfriSAR study. The is one step close to a comprehensive AGB model for the global. 
	
Study Area and Data Sets 
Site Description and Field data 
	The Study site that is located in the Mondah Forest in Gabon which is part of the 2016 AfriSAR Campaign. The field data was collected from 15 1-hectare plots. These plots were sub divided into .0625 ha and .25ha plots. Each of this had  basal area, aboveground biomass, number of trees per plot, maximum tree height, and basal-area-weighted wood specific gravity aggregated to them. 
	Along with the plots tree level data is also provided.  Family and species of each tree was determined by a local botanist. DBH is the Diameter at Breast Height measured with a diameter measurement tape at 1.3 m height. Tree height measured in the field with DBH meter and a clinometer. Biomass of each tree is estimated using the equation with tree diameter (Chave , Rejou-Mechain, et al. 2015), wood specific gravity (defined by tree species) and tree height. 
LiDAR data 
LVIS
 	LVIS is a waveform lidar system that is mounted on an aircraft. It has a 25 meter laser foot print that collects a swath that is 2000 meters. It does this by swiping the sensor left to right as the plan fly overhead. the LVIS mission has two type of data production the L1B Geolocated Waveform and the L2 Elevation and Height Product. 
	L1B is the wave form data id the .h5 file that has the raw rxwave data. Rxwave is the return waveform at 1028 samples. 
	L2B is a processed TXT file that has preposed RH values. The RH value are the Return Height values. 

GEDI
	GEDI is a full-waveform lidar instrument that is deployed on the Japanese Experimental Module – Exposed Facility (JEM-EF) aboard the International space station (ISS). GEDI comes in three different data products. Level 1B Geolocated Waveforms, Level 2A Elevation and Height Metrics,  and Level 2B Canopy Cover and Vertical Profile Metrics.
	The L1B data product provides geolocated and smooth forms for each shot in the all eight GEDI Beams. The L1B has a average footprint of 25 which is the same as LVIS. 
	The L2A product works with Elevation and Height Metrics. This provides waveform interpretation and extracted products from each GEDI waveform. This includes ground elevation, canopy height, and relative return energy metrics. 
	The last is the L2B product. This provided derived metrics from the L1B product and includes canopy cover, Plant Area Index (PAI), Plant Area Volume Density (PAVD) and Foliage Height Diversity (FHD).  

	
DATA Processing
Aircraft data 
	This LVIS data is organized by based on the data and time of each of the flight. To find the LVIS Lidar shot that correspond to the with the 15 field plot the flight path data is used. First GIS is used to the day flights of the needed flighted. Once that is found the L2 Data type can be converted to points. Find the point that fall with in each other plots. The waveform L1 product can be downloaded. Once the waveform data that is with in the study sites they can be downloads. 
Spaceborne data 
	This need to be researched
LiDAR analysis
LVIS 
RH and AGB
The Goal of this project is come up with biomass index for these trees like the canopy cover, Plant Area Index (PAI), Plant Area Volume Density (PAVD) and Foliage Height Diversity (FHD) of L2B product for the Biomass index with both LVIS data and GEDI data. 
The first comparing the RH value with the AGB mass for each of the LVIS shots. This is then done at plot, .25 plot and the .0625 plot level. The is done by given all of the 
Waveform 

Biomass Index 
GEDI


Results 

Discussion 

Conclusion 
