#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 17, 2020

This script was used to create and evaluate skewed normal and lognormal 
distribution fits of the data sets using bayesian optimization. 

The data set includes X, Y, Z coordinates of a data point. 
The "size" or the value of this data point.
And "distance" and "elevation" attributes assigned to each data plot. 

For a descriptions of the importance of these data, extracted from ArcMap, 
I refer to Scheller & Ehlmann (2020), JGR

Mean, std, variance, kurtosis, skewness, and probability distributions were 
calculated in order to evaluate changes to distributions with different 
"distance" and "elevation" bins.

Author: Eva L. Scheller, email: eschelle@caltech.edu
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm
from scipy.stats import skewnorm

#Below I am reading in 13 different data sets
#Each data set includes a size and distance characteristic
#As well as a X,Y,Z coordinate, here Z refers to the elevation coordinate of each data point
#Here you could load in your data instead

#Mb57597475
D_mb75597475 = np.genfromtxt('Data/mb75597475_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb75597475 = list(D_mb75597475[:,3])
distances_mb75597475 = list(D_mb75597475[:,11])
Z_mb75597475 = list(D_mb75597475[:,16])
X_mb75597475=list(D_mb75597475[:,17])
Y_mb75597475=list(D_mb75597475[:,18])

#Mb117
D_mb117 = np.genfromtxt('Data/mb117_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb117 = list(D_mb117[:,2])
distances_mb117 = list(D_mb117[:,8])
Z_mb117 = list(D_mb117[:,14])
X_mb117=list(D_mb117[:,12])
Y_mb117=list(D_mb117[:,13])

#Mb88
D_mb88 = np.genfromtxt('Data/mb88_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb88 = list(D_mb88[:,2])
distances_mb88 = list(D_mb88[:,8])
Z_mb88 = list(D_mb88[:,12])
X_mb88 =list(D_mb88[:,13])
Y_mb88 =list(D_mb88[:,14])

#Mb54
D_mb54 = np.genfromtxt('Data/mb54_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb54 = list(D_mb54[:,4])
distances_mb54 = list(D_mb54[:,10])
Z_mb54 = list(D_mb54[:,16])
X_mb54 =list(D_mb54[:,17])
Y_mb54 =list(D_mb54[:,18])

#Mb123
D_mb123 = np.genfromtxt('Data/mb123_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb123 = list(D_mb123[:,2])
distances_mb123 = list(D_mb123[:,8])
Z_mb123 = list(D_mb123[:,12])
X_mb123 =list(D_mb123[:,13])
Y_mb123 =list(D_mb123[:,14])

#Mb92
D_mb92 = np.genfromtxt('Data/mb92_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb92 = list(D_mb92[:,2])
distances_mb92 = list(D_mb92[:,8])
Z_mb92 = list(D_mb92[:,12])
X_mb92 =list(D_mb92[:,13])
Y_mb92 =list(D_mb92[:,14])

#Mb186
D_mb186 = np.genfromtxt('Data/mb186_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb186 = list(D_mb186[:,1])
distances_mb186 = list(D_mb186[:,7])
Z_mb186 = list(D_mb186[:,12])
X_mb186 =list(D_mb186[:,13])
Y_mb186 =list(D_mb186[:,14])

#Mb105
D_mb105 = np.genfromtxt('Data/mb105_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb105 = list(D_mb105[:,2])
distances_mb105 = list(D_mb105[:,8])
Z_mb105 = list(D_mb105[:,12])
X_mb105 =list(D_mb105[:,13])
Y_mb105 =list(D_mb105[:,14])

#Mb102
D_mb102 = np.genfromtxt('Data/mb102_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb102 = list(D_mb102[:,2])
distances_mb102 = list(D_mb102[:,8])
Z_mb102 = list(D_mb102[:,13])
X_mb102 =list(D_mb102[:,14])
Y_mb102 =list(D_mb102[:,15])

#Mb79
D_mb79 = np.genfromtxt('Data/mb79_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb79 = list(D_mb79[:,2])
distances_mb79 = list(D_mb79[:,8])
Z_mb79 = list(D_mb79[:,12])
X_mb79 =list(D_mb79[:,13])
Y_mb79 =list(D_mb79[:,14])

#Mb78
D_mb78 = np.genfromtxt('Data/mb78_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb78 = list(D_mb78[:,4])
distances_mb78 = list(D_mb78[:,10])
Z_mb78 = list(D_mb78[:,16])
X_mb78 =list(D_mb78[:,17])
Y_mb78 =list(D_mb78[:,18])

#Mb84835
D_mb84835 = np.genfromtxt('Data/mb84835_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb84835 = list(D_mb84835[:,3])
distances_mb84835 = list(D_mb84835[:,9])
Z_mb84835 = list(D_mb84835[:,14])
X_mb84835 =list(D_mb84835[:,15])
Y_mb84835 =list(D_mb84835[:,16])

#Mb32
D_mb32 = np.genfromtxt('Data/mb32_master_table.txt',delimiter='\t',skip_header=1)
sizes_mb32 = list(D_mb32[:,2])
distances_mb32 = list(D_mb32[:,8])
Z_mb32 = list(D_mb32[:,12])
X_mb32 =list(D_mb32[:,13])
Y_mb32 =list(D_mb32[:,14])

#Create master arrays
#Here I converge all of my X, Y, Z of my data points and their size characteristics into 4 arrays
#I will use these arrays in subsequent work
X = X_mb75597475+X_mb117+X_mb88+X_mb54+X_mb123+X_mb92+X_mb186+X_mb105+X_mb102+X_mb79+X_mb78+X_mb84835+X_mb32
Y=Y_mb75597475+Y_mb117+Y_mb88+Y_mb54+Y_mb123+Y_mb92+Y_mb186+Y_mb105+Y_mb102+Y_mb79+Y_mb78+Y_mb84835+Y_mb32
Z=Z_mb75597475+Z_mb117+Z_mb88+Z_mb54+Z_mb123+Z_mb92+Z_mb186+Z_mb105+Z_mb102+Z_mb79+Z_mb78+Z_mb84835+Z_mb32
sizes = sizes_mb75597475+sizes_mb117+sizes_mb88+sizes_mb54+sizes_mb123+sizes_mb92+sizes_mb186+sizes_mb105+sizes_mb102+sizes_mb79+sizes_mb78+sizes_mb84835+sizes_mb32
distances = distances_mb75597475 + distances_mb117+distances_mb88+distances_mb54+distances_mb123+distances_mb92+distances_mb186+distances_mb105+distances_mb102+distances_mb79+distances_mb78+distances_mb84835+distances_mb32
elevations = Z

#In this project I wanted to look for investigations in the sizes characteristic with distances and elevations
#Therefore I sorted my sizes in distance and elevation intervals below
size_lessthan700 = []
size_700_750=[]
size_750_800=[]
size_800_850=[]
size_850_900=[]
size_900_950=[]
size_950_1000=[]
size_1000_1050=[]
size_1050_1100 = []
size_over1100 = []
for i in range(len(distances)):
    if distances[i] < 750000 and distances[i] > 700000:
        size_700_750.append(sizes[i])
    if distances[i] < 800000 and distances[i] > 750000:
        size_750_800.append(sizes[i])
    if distances[i] < 850000 and distances[i] > 800000:
        size_800_850.append(sizes[i])
    if distances[i] < 900000 and distances[i] > 850000:
        size_850_900.append(sizes[i])
    if distances[i] < 950000 and distances[i] > 900000:
        size_900_950.append(sizes[i])
    if distances[i] < 1000000 and distances[i] > 950000:
        size_950_1000.append(sizes[i])
    if distances[i] < 1050000 and distances[i] > 1000000:
        size_1000_1050.append(sizes[i])
    if distances[i] < 1100000 and distances[i] > 1050000:
        size_1050_1100.append(sizes[i])

size_0_200 = []
size_200_400=[]
size_400_600=[]
size_600_800=[]
size_800_1000=[]
size_1000_1200=[]
size_1200_1400=[]
size_1400_1600=[]
size_1600_1800 = []
size_1800_2000 = []
size_2000_2200 = []
size_2200_2400 = []
size_2400_2600 = []
for i in range(len(elevations)):
    if -elevations[i] < 200:
        size_0_200.append(sizes[i])
    if -elevations[i] < 400 and -elevations[i] > 200:
        size_200_400.append(sizes[i])
    if -elevations[i] < 600 and -elevations[i] > 400:
        size_400_600.append(sizes[i])
    if -elevations[i] < 800 and -elevations[i] > 600:
        size_600_800.append(sizes[i])
    if -elevations[i] < 1000 and -elevations[i] > 800:
        size_800_1000.append(sizes[i])
    if -elevations[i] < 1200 and -elevations[i] > 1000:
        size_1000_1200.append(sizes[i])
    if -elevations[i] < 1400 and -elevations[i] > 1200:
        size_1200_1400.append(sizes[i])
    if -elevations[i] < 1600 and -elevations[i] > 1400:
        size_1400_1600.append(sizes[i])
    if -elevations[i] < 1800 and -elevations[i] > 1600:
        size_1600_1800.append(sizes[i])
    if -elevations[i] < 2000 and -elevations[i] > 1800:
        size_1800_2000.append(sizes[i])
    if -elevations[i] < 2200 and -elevations[i] > 2000:
        size_2000_2200.append(sizes[i])
    if -elevations[i] < 2400 and -elevations[i] > 2200:
        size_2200_2400.append(sizes[i])
    if -elevations[i] < 2600 and -elevations[i] > 2400:
        size_2400_2600.append(sizes[i])

#These arrays represent all of the sorted data in distance and elevation intervals
size_nest_distances = [size_700_750,size_750_800,size_800_850,size_850_900,size_900_950,size_950_1000,size_1000_1050,size_1050_1100]
size_nest_elevations = [size_0_200,size_200_400,size_400_600,size_600_800,size_800_1000,size_1000_1200,size_1200_1400,size_1400_1600,size_1600_1800,size_1800_2000,size_2000_2200,size_2200_2400,size_2400_2600]

#First, I want to get a general sense of means and medians of the data set for
#each distance and elevation bin when assuming a gaussian distribution
#Numpy mean and median assumptions are gaussian distributions
#Now I use my nested lists to calculate the gaussian mean and median of each bin
size_nest_elevations_median = []
size_nest_elevations_mean = []
size_nest_distance_median = []
size_nest_distance_mean = []
for i in size_nest_elevations:
    size_nest_elevations_median.append(np.median(i)) #calculate median for elevation bins
    size_nest_elevations_mean.append(np.mean(i)) #calculate  mean for elevation bins
size_nest_distance_median = []
for i in size_nest_distances:
    size_nest_distance_median.append(np.median(i)) #calculate median for distance bins
    size_nest_distance_mean.append(np.mean(i)) #calculate  mean for distance bins

elevations_intervals = [-100,-300,-500,-700,-900,-1100,-1300,-1500,-1700,-1900,-2100,-2300,-2500] #Median of each bin for plotting
distance_intervals = [725,775,825,875,925,975,1025,1075] #Median of each bin for plotting

#I now contruct figures that look at the full data set for each distance bin in grey 
#Means are plotted in blue
#Medians are plotted in red
plt.figure(1)
plt.plot([725]*len(size_700_750),size_700_750,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0,label='All data')
plt.plot([775]*len(size_750_800),size_750_800,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([825]*len(size_800_850),size_800_850,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)#plt.subplot(1,2,2)
plt.plot([875]*len(size_850_900),size_850_900,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([925]*len(size_900_950),size_900_950,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)#plt.subplot(1,2,2)
plt.plot([975]*len(size_950_1000),size_950_1000,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([1025]*len(size_1000_1050),size_1000_1050,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)#plt.subplot(1,2,2)
plt.plot([1075]*len(size_1050_1100),size_1050_1100,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot(distance_intervals,size_nest_distance_mean,'o',color='blue',markersize=10.0,label='Sizes mean')
plt.plot(distance_intervals,size_nest_distance_median,'o',color='red',markersize=10.0,label='Sizes median')
plt.xlabel('Distance bin median')
plt.ylabel('sizes (m)')
plt.title('Gaussian mean and median of sizes in distance bins')
plt.legend()

#I now contruct figures that look at the full data set for each elevation bin in grey 
#Means are plotted in blue
#Medians are plotted in red
plt.figure(2)
plt.plot([-100]*len(size_0_200),size_0_200,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0,label='All data')
plt.plot([-300]*len(size_200_400),size_200_400,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-500]*len(size_400_600),size_400_600,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-700]*len(size_600_800),size_600_800,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-900]*len(size_800_1000),size_800_1000,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-1100]*len(size_1000_1200),size_1000_1200,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-1300]*len(size_1200_1400),size_1200_1400,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-1500]*len(size_1400_1600),size_1400_1600,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-1700]*len(size_1600_1800),size_1600_1800,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-1900]*len(size_1800_2000),size_1800_2000,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-2100]*len(size_2000_2200),size_2000_2200,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-2300]*len(size_2200_2400),size_2200_2400,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.plot([-2500]*len(size_2400_2600),size_2400_2600,'o',color='grey',markeredgecolor='black',markeredgewidth=1.0)
plt.xticks([-2400,-2200,-2000,-1800,-1600,-1400,-1200,-1000,-800,-600,-400,-200])
plt.plot(elevations_intervals,size_nest_elevations_mean,'o',color='blue',markersize=10.0,label='Sizes mean')
plt.plot(elevations_intervals,size_nest_elevations_median,'o',color='red',markersize=10.0,label='Sizes median')
plt.xlabel('Elevation bin median')
plt.ylabel('sizes (m)')
plt.title('Gaussian mean and median of sizes in elevation bins')
plt.legend()
        
#Since I don't expect the distributions to be gaussian
#I want to investigate what the data would look like when approximated with skewed normal distributions
#First I plot all fitted skewed normal distributions through distance bins
#The skewed normal distributions are fitted through Bayesian optimization using the scipy module
plt.figure(3)
plt.xlabel('distance bin')
plt.ylabel('sizes (m)')
n=1
x = np.arange(0,200,0.1) #range needed to create probability distribution function
skewed_mean_distances = []
skewed_std_distances = []
skewed_variance_distances = []
skewed_kurtosis_distances = []
skewed_skew_distances = []
for bins in size_nest_distances:
    if len(bins) > 10:
        a,loc,scale = skewnorm.fit(bins) #I fit all distance bins 
        mean,var,skew,kurt = skewnorm.stats(a,loc,scale,moments='mvsk')
        skewed_mean_distances.append(mean)
        skewed_std_distances.append(skewnorm.std(a,loc,scale)) #Calculate the std of all distributions
        skewed_variance_distances.append(var) #Calcualate variance if interesting
        skewed_skew_distances.append(skew) #calculate skewness if interesting
        skewed_kurtosis_distances.append(kurt) #calculate kurtosis if interesting
        pdf=skewnorm.pdf(x,a,loc,scale) #create probability distribution function
        #I now plot all of the fitted distributions with their respective histograms
        plt.subplot(1,len(size_nest_distances),n)
        plt.hist(bins,bins=50,normed=True)
        plt.plot(x,pdf)
        n+=1
        plt.title('Skewed normal')
        plt.xlabel('distance bin {}'.format(n))
        plt.ylabel('sizes (m)')
        
#Small program below to correct for the fact that one of my bins is empty
for i in range(len(size_nest_distances)):
   if len(size_nest_distances[i]) < 10:
       distance_intervals.pop(i) 
    
#Now I can plot means and std calculated from skewed normal distributions
#Similar plots could be done for variance, skewness, and kurtosis if interesting
#In this project I was mostly interested in the means
plt.figure(4)
plt.errorbar(distance_intervals,skewed_mean_distances,yerr=skewed_std_distances,fmt='o')
plt.xlabel('Median of distance intervals (m)')
plt.ylabel('Mean size (m)')
plt.title('Calculated means and std of distance intervals w. skewed norm distribution')     
#Figure 4 is an example of a plot that can easily be made for skewness, kurtosis, and variation
#and subsequently fitted distributions

#We can now repeat the same analysis with elevation bins
#Here I want to compare all of the distributions directly so instead of making subplots
#I create one big plot for visual comparison
plt.figure(5) 
plt.title('Skewed normal distributions of elevation bins')
plt.ylabel('Sizes (m)')
plt.xlabel('Elevation bins')
plt.ylim(0,0.1)
n=1
skewed_mean_elevations = []
skewed_std_elevations = []
skewed_variance_elevations = []
skewed_kurtosis_elevations = []
skewed_skew_elevations = []
for bins in size_nest_elevations: 
    if len(bins) > 10:
        a,loc,scale = skewnorm.fit(bins)
        mean,var,skew,kurt = skewnorm.stats(a,loc,scale,moments='mvsk')
        skewed_mean_elevations.append(mean)
        skewed_variance_elevations.append(var)
        skewed_skew_elevations.append(skew)
        skewed_kurtosis_elevations.append(kurt)
        skewed_std_elevations.append(skewnorm.std(a,loc,scale))
        pdf=skewnorm.pdf(x,a,loc,scale)
        plt.plot(x,pdf,label='{}'.format(n))
        #If comparison to histograms is interesting uncomment line below
        #plt.hist(bins,bins=50,normed=True)
        n+=1
plt.xlabel('elevation (m)') 
plt.ylabel('sizes (m)')


#Next, I am interested in understand how lognormal fits would approximate
#the data instead of skewed normal fits, so I repeat the analysis with lognormal fits
plt.figure(6) 
plt.title('Lognormal distributions of distance bins')
plt.ylabel('Sizes (m)')
plt.xlabel('Distance (m)')
plt.ylim(0,0.125)
n=1
lognorm_mean_distance = []
lognorm_var_distance = []
lognorm_skew_distance = []
lognorm_kurt_distance = []
for bins in size_nest_distances: 
    if len(bins) > 10:
        s,loc,scale = lognorm.fit(bins)
        mean,var,skew,kurt = lognorm.stats(s,loc,scale,moments='mvsk')
        lognorm_mean_distance.append(mean)
        lognorm_var_distance.append(var)
        lognorm_skew_distance.append(skew)
        lognorm_kurt_distance.append(kurt)
        pdf=lognorm.pdf(x,s,loc,scale)
        plt.plot(x,pdf,label='{}'.format(n)) #In this plot I am plotting all distributions together
    n+=1
plt.legend()

plt.figure(7)
plt.title('Lognormal distributions of distance bins')
plt.ylabel('Sizes (m)')
plt.xlabel('Distance bin (m)')
n=1
x = np.arange(0,200,0.1)
for bins in size_nest_distances:
    if len(bins) > 10:
        s,loc,scale = lognorm.fit(bins)
        pdf=lognorm.pdf(x,s,loc,scale)
        plt.subplot(1,len(size_nest_distances),n) #In this plot I plot distributions separately with histograms
        plt.title('lognormal')
        plt.hist(bins,bins=50,normed=True)
        plt.plot(x,pdf)
        plt.xlabel('distance bin {}'.format(n))
        plt.ylabel('sizes (m)')
        n+=1

plt.figure(8) 
plt.title('Lognormal distributions of elevations bins')
plt.ylabel('Sizes (m)')
plt.xlabel('Distance (m)')
plt.ylim(0,0.125)
n=1
lognorm_mean_elevations = []
lognorm_var_elevations = []
lognorm_kurtosis_elevations = []
lognorm_skew_elevations = []
for bins in size_nest_elevations: 
    if len(bins) > 10:
        s,loc,scale = lognorm.fit(bins)
        mean,var,skew,kurt=lognorm.stats(s,loc,scale,moments='mvsk')
        lognorm_mean_elevations.append(mean)
        lognorm_var_elevations.append(var)
        lognorm_kurtosis_elevations.append(kurt)
        lognorm_skew_elevations.append(skew)
        pdf=lognorm.pdf(x,s,loc,scale)
        plt.plot(x,pdf,label='{}'.format(n))
    n+=1
plt.legend()

plt.show()


