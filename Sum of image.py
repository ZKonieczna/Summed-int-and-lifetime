# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:44:24 2021

@author: s1505470
"""

from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np
from skimage.io import imread
from skimage import filters,measure
import matplotlib.pyplot as plt
import napari



# Convert to wavelength- thede are from the fits to the TS Bead Data. 
m=0.5253
c=473.38

# Read the files 

mat_fname=r"D:\AA3_cubes\20210330_AA3AA4_dioxane_0_hist1_ROI2\Lifetime_Data/LifetimeImageData.mat"
mat_contents = sio.loadmat(mat_fname,squeeze_me=True)
lifetimes0=mat_contents['lifetimeImageData']


mat_fname=r"D:\AA3_cubes\20210330_AA3AA4_dioxane_0_hist1_ROI2\Lifetime_Data/LifetimeAlphaData.mat"
mat_contents2 = sio.loadmat(mat_fname,squeeze_me=True)
intensities0=mat_contents2['lifetimeAlphaData']



# This is to make an average of lifetime/intensity across all image pixels
mean_int0=np.mean(intensities0,axis=(1,2))
mean_intstd0=np.std(intensities0, axis=(1,2))

mean_int_high=mean_int0+mean_intstd0
mean_int_low=mean_int0-mean_intstd0


x_axis=np.linspace(0,511,512)
x_axis_correct=c+m*x_axis

plt.plot(x_axis_correct,mean_int0,label="Mean")
plt.plot(x_axis_correct,mean_int_high,label="Mean+Std")
plt.plot(x_axis_correct,mean_int_low,label="Mean-Std")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
##plt.ylim([0,1000])
plt.xlim([475,740])
plt.legend()
plt.show()   



###IGNORE FOR NOW

plt.plot(x_axis_correct,mean_lifetime0,label="0% dioxane")
plt.plot(x_axis_correct,mean_lifetime20,label="20% dioxane")
plt.plot(x_axis_correct,mean_lifetime40,label="40% dioxane")
plt.plot(x_axis_correct,mean_lifetime60,label="60% dioxane")
plt.plot(x_axis_correct,mean_lifetime80,label="80% dioxane")
plt.plot(x_axis_correct,mean_lifetime100,label="100% dioxane")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Lifetime (ns)")
plt.ylim([0,1])
plt.xlim([540,640])
plt.legend()
plt.show()   
        