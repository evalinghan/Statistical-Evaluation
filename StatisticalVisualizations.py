#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 17 2020

This script produces different statistical visualizations of a data set. 
These visualizations include 4D plots, violin plots, and boxplots.

The data set includes X, Y, Z coordinates of a data point. 
The "size" or the value of this data point.
And "distance" and "elevation" attributes assigned to each data plot. 

For a descriptions of the importance of these data, extracted from ArcMap, 
I refer to Scheller & Ehlmann (2020), JGR

@author: evascheller
"""
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np
import seaborn as sns
import pandas as pd

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

#Firt, I plot a 4D plot that shows the X, Y, Z coordinates of my points as well as a heatmap of their values
fig1=plt.figure()
ax=fig1.add_subplot(111,projection='3d')
h=ax.scatter(X,Y,Z,c=sizes,cmap=cm.jet,norm=matplotlib.colors.LogNorm())
fig1.colorbar(h, label='sizes (m)')
ax.set_xlabel('X-coordinate (m)')
ax.set_ylabel('Y-coordinate (m)')
ax.set_zlabel('Z-coordinate (m)')

#I also wanted to look at the variation in the sizes characteristics compared to distances and elevations (Z-coordinate)
fig2=plt.figure()
ax=fig2.add_subplot(111)
g=ax.scatter(distances,elevations,c=sizes,marker='o',cmap=cm.jet,norm=matplotlib.colors.LogNorm())
fig2.colorbar(g, label='sizes (m)')
ax.set_xlabel('Distances (m)')
ax.set_ylabel('Elevations (m)')

#Second, I plot a violinplot that shows the distribution of all the data points
plt.figure(3)
plt.title('Violin plot of all data points')
sns.set()
df0=pd.DataFrame([sizes],['All data']).T
sns.violinplot(data=df0)
plt.ylabel('sizes (m)')

#In this project I wanted to look for investigations in the sizes characteristic with distances and elevations
#Therefore I sorted my sizes in distance and elevation intervals below
size_700_725=[]
size_725_750=[]
size_750_775=[]
size_775_800=[]
size_800_825=[]
size_825_850=[]
size_850_875=[]
size_875_900=[]
size_900_925=[]
size_925_950=[]
size_950_975=[]
size_975_1000=[]
size_1000_1025=[]
size_1025_1050=[]
size_1050_1075=[]
size_1075_1100=[]
for i in range(len(distances)):
    if distances[i] < 725000 and distances[i] > 700000:
        size_700_725.append(sizes[i])
    if distances[i] < 750000 and distances[i] > 725000:
        size_725_750.append(sizes[i])
    if distances[i] < 775000 and distances[i] > 750000:
        size_750_775.append(sizes[i])
    if distances[i] < 800000 and distances[i] > 775000:
        size_775_800.append(sizes[i])
    if distances[i] < 825000 and distances[i] > 800000:
        size_800_825.append(sizes[i])
    if distances[i] < 850000 and distances[i] > 825000:
        size_825_850.append(sizes[i])
    if distances[i] < 875000 and distances[i] > 850000:
        size_850_875.append(sizes[i])
    if distances[i] < 900000 and distances[i] > 875000:
        size_875_900.append(sizes[i])
    if distances[i] < 925000 and distances[i] > 900000:
        size_900_925.append(sizes[i])
    if distances[i] < 950000 and distances[i] > 925000:
        size_925_950.append(sizes[i])
    if distances[i] < 975000 and distances[i] > 950000:
        size_950_975.append(sizes[i])
    if distances[i] < 1000000 and distances[i] > 975000:
        size_975_1000.append(sizes[i])
    if distances[i] < 1025000 and distances[i] > 1000000:
        size_1000_1025.append(sizes[i])
    if distances[i] < 1050000 and distances[i] > 1025000:
        size_1025_1050.append(sizes[i])
    if distances[i] < 1075000 and distances[i] > 1050000:
        size_1050_1075.append(sizes[i])
    if distances[i] < 1100000 and distances[i] > 1075000:
        size_1075_1100.append(sizes[i])

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
size_nest_distances = [size_700_725,size_725_750,size_750_775,size_775_800,size_800_825,size_825_850,size_850_875,size_875_900,size_900_925,size_925_950,size_950_975,size_975_1000,size_1000_1025,size_1025_1050,size_1050_1075,size_1075_1100]
size_nest_elevations = [size_0_200,size_200_400,size_400_600,size_600_800,size_800_1000,size_1000_1200,size_1200_1400,size_1400_1600,size_1600_1800,size_1800_2000,size_2000_2200,size_2200_2400,size_2400_2600]
    
#I can now construct data frames of these binned arrays 
df1=pd.DataFrame(size_nest_distances,['700_725','725_750','750_775','775_800','800_825','825_850','850_875','875_900','900_925','925_950','950_975','975_1000','1000_1025','1025_1050','1050_1075','1075_1100']).T
df2=pd.DataFrame((size_nest_elevations),['-0-200','-200-400','-400-600','-600-800','-800-1000','-1000-1200','-1200-1400','-1400-1600','-1600-1800','-1800-2000','-2000-2200','-2200-2400','-2400-2600']).T

#Last I construct boxplots and violin plots of these distance and elevation bins
plt.figure(4)
sns.set()
sns.violinplot(data=df1)
plt.title('Violin plots of sizes in distance bins')
plt.ylabel('sizes (m)')

plt.figure(5)
sns.set()
sns.violinplot(data=df2)
plt.title('Violin plots of sizes in elevation bins')
plt.ylabel('sizes (m)')

plt.figure(6)
plt.boxplot(size_nest_distances)
plt.title('Box plots of sizes in distance bins')
plt.ylabel('sizes (m)')


plt.figure(7)
plt.boxplot(size_nest_elevations)
plt.title('Box plots of sizes in elevation bins')
plt.ylabel('sizes (m)')


plt.show()



