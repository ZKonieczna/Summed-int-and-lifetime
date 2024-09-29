# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:34:06 2021

@author: s1505470
"""


from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import napari

#first bit imports .mat data
#it also compresses cubes into 2D matrices for processing
#done both for Intensity and Lifetime Data

mat_fname=r"D:\20210409_Maria\MR28_2\Lifetime_Data\LifetimeImageData.mat"
mat_contents = sio.loadmat(mat_fname,squeeze_me=True)
lifetimes=mat_contents['lifetimeImageData']


mat_fname=r"D:\20210409_Maria\MR28_2\Lifetime_Data\LifetimeAlphaData.mat"
mat_contents2 = sio.loadmat(mat_fname,squeeze_me=True)
intensities=mat_contents2['lifetimeAlphaData']


mat_fname=r"D:\20210409_Maria\MR28_noenzyme_2\Lifetime_Data\LifetimeImageData.mat"
mat_contents3 = sio.loadmat(mat_fname,squeeze_me=True)
lifetimes_NIT=mat_contents3['lifetimeImageData']


mat_fname=r"D:\20210409_Maria\MR28_noenzyme_2\Lifetime_Data\LifetimeAlphaData.mat"
mat_contents4 = sio.loadmat(mat_fname,squeeze_me=True)
intensities_NIT=mat_contents4['lifetimeAlphaData']

def see(number):
    plane=lifetimes[number]
    plt.imshow(plane)
   
    return plane
   
def plot(x,y):
    intensity_pixels = [] 
        
    for i in range(len(intensities)):
        intensities_value=intensities[i][187][188]
        intensity_pixel.append(intensities_value)
        plt.plot(intensities_value)
        plt.show()
       
    return intensity_pixels


#this bit opens data in Napari, frame/wavelength 30 chosen aribitrarly, for ease of processing

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(intensities[130])
    viewer.add_image(lifetimes[130])


#downloads labels and data points from Napari     
labels = viewer.layers["Labels"].data    

lifetime_values=[] #creates a matrix of 512 pixels

#next bit opens any lifetime value that was labelled
#calculates a mean of the labelled region
#does so for each of the 512 wavlengths, and attaches data together so you can plot it
for i in range(len(lifetimes)):
    label_number=1 #change according to what you need
    lifetime_label=lifetimes[i][labels==label_number]
    lifetime_av=lifetime_label.mean()
    lifetime_values.append(lifetime_av)
    

lifetime_NIT=[] #creates a matrix of 512 pixels

#next bit opens any lifetime value that was labelled
#calculates a mean of the labelled region
#does so for each of the 512 wavlengths, and attaches data together so you can plot it
for i in range(len(lifetimes_NIT)):
    label_number=1
    lifetime_label=lifetimes_NIT[i][labels==label_number]
    lifetime_std=lifetime_label.mean()
    lifetime_NIT.append(lifetime_std)

#after creating mean and std data sets, defining axes below
y_axis=lifetime_values
y_axis2=lifetime_NIT
x_axis=np.linspace(0,511,512) #creates numbers between 1-512

m=0.5253 #parameters from bead plots
c=473.38

x_axis_correct=c+m*x_axis #correct equation

#now plot using the correct x axis

plt.plot(x_axis_correct,y_axis,label="MR28")
plt.plot(x_axis_correct,y_axis2,label="MR28_no_enzyme")
plt.xlabel("wavelength (nm)")
plt.ylabel("Lifetime (ns)")
plt.xlim([475,520])

plt.legend()
plt.show()   


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(intensities[130])
    viewer.add_image(intensities_NIT[130])


#downloads labels and data points from Napari     
labels = viewer.layers["Labels"].data    



    
intensity_values=[]

for i in range(len(intensities)):
    label_number=1
    intensity_label=intensities[i][labels==label_number]
    intensity_av=intensity_label.mean()
    intensity_values.append(intensity_av)

    
#same as above, but intensities instead

intensity_NIT=[]    
    
for i in range(len(intensities_NIT)):
    label_number=1
    lifetimes_label=intensities_NIT[i][labels==label_number]
    intensity_std=lifetimes_label.mean()
    intensity_NIT.append(intensity_std)

        
y_axis=intensity_values
y_axis2=intensity_NIT
x_axis=np.linspace(0,511,512)

m=0.5253
c=473.38

x_axis_correct=c+m*x_axis

plt.plot(x_axis_correct,y_axis,label="MR28")
plt.plot(x_axis_correct,y_axis2,label="MR28_no_enzyme")
plt.xlabel("wavelength (nm)")
plt.ylabel("Intensity")
plt.xlim([475,600])
plt.legend()
plt.show()    