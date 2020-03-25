# Statistical Evaluations

For this project, I had extracted a data set of rock sizes from Mars sattelite imagery at various distances and elevations of an impact crater. 
I was interested in understanding whether there were any systematic changes in the rock sizes with variations in the recorded distances and elvations.  
I solved this problem by using data visualization, performing statistical tests, and investigation bayesian distribution fits of binned data.  

In this directory, you'll find 3 python scripts: 

StatisticalVisualizations.py

MannWhitneyUtest.py

DistributionFits.py

Example data for the project can be found in the data directory.
These scripts are supposed to be used in the following order.


## StatisticalVisualizations

This script is used to construct 4D histograms, violin plots, and boxplots for a quick visualization of data.  
You will need the following packages for this script: seaborn and pandas. 


## MannWhitneyUtest

This script was used to make a first order estimate on whether distributions within different bins of data were statistically significant. 
You will need the scipy package for this script. 

## DistributionFits

This was used to make skewed normal and lognormal distribution fits for different bins of data in order to compare distributions and their moments.
You will need the scipy package for this script.
