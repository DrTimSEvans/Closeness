'''
Plots and Analysis MoreDAtaSets files for closeness paper
@author: time
'''

import math

# Useful for manipulating filenames without worrying about which OS you use
import os

# Useful for many things
import numpy as np


# Plot library produces excellent high quality plots and emulates MatLab (which may or may not be of use to you)
# I would think of using python/matplotlib for plotting even if you do your sums in another language
# for plot tutorial see http://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

# see http://matplotlib.org/api/pyplot_api.html
# fontsize in points try 12 for a4 paper 18 or 24 for overheads
fs=24
# plot marker size in pts, use as markersize=ms
ms=10

# I find that UNIX style forward slashes work on any OS in most languages
# They should be backwards slashes on Windows but a backwards slash has a special meaning
# so I recommend just using a forwards slash where a backwards would be used on Windows
# This is the directory where I want my outputs to go
# MAKE SURE DIRECTORY EXISTS!
# outputdir='h:/CandN/output/"

outputdir="./output/"
inputdir="./input/"
filenameroot="MoreDataSets220127"


# ***********************************************************

fullinputfilename=os.path.join(inputdir,filenameroot+".dat")
print '--- Reading network data from ',fullinputfilename




# ***************************************************
# Simple unit size bins
# numpy.arange(start, stop, step) used to set bin edges at half integers
simplebins=np.arange(kmin-0.5,kmax+0.5,1.0)
simplehist, simplebinedges = np.histogram(degreelist,density=True, bins=simplebins)
simplebincentres=range(kmin,kmax,1)

#print simplebincentres

# .........................
# Plots simple data
fig1= plt.figure() # start a new plot and give it an number, starts from 0 and increments otherwise
ax = plt.subplot(111) # seems to create a 1 by 1 grid in figure 1 but it gives you access to the axes
ax.set_xscale('log')
ax.set_yscale('log')

plt.plot(simplebincentres,simplehist,'x',color='black')

plt.xlabel('$k$', fontsize=fs)
plt.ylabel(r'$p(k)$', fontsize=fs)
plt.title(datatitle, fontsize=fs)

#plt.legend()

filenamewext=filenameroot+"ddsimple"

ext=".eps"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
ext=".pdf"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
#plt.show()



# *********************************************
# Now set up log binning
rvalue=1.1

k=float(kmin)-0.5 # this will be float value, current logbin location
logbinvalues=[k] 
logbincentres=[ ]
logbinwidth=[ ]
while k<=kmax:
    knew=int(k*rvalue)+0.5 # must ensure this is a half integer
    # must ensure logbin is at least 1.0 wide
    if knew<=(k+1.0):
        knew=k+1.0
    logbinvalues.append(knew)
    logbincentres.append((k+knew)/2) # could also use geometric mean    
    logbinwidth.append(knew-k) 
    k=knew

logbinhist, logbinedges = np.histogram(degreelist, bins=logbinvalues, density=True)


# .........................
plt.figure() # start a new plot and give it an number, starts from 0 and increments otherwise
ax = plt.subplot(111) # seems to create a 1 by 1 grid in figure 1 but it gives you access to the axes
ax.set_xscale('log')
ax.set_yscale('log')
plt.plot(simplebincentres,simplehist,'x',color='black',label='raw')
plt.plot(logbincentres,logbinhist,'o',color='red',label='log binned')

plt.xlabel('$k$', fontsize=fs)
plt.ylabel(r'$p(k)$', fontsize=fs)
plt.title(datatitle, fontsize=fs)

plt.legend()

filenamewext=filenameroot+"ddsimplelogbin"

ext=".eps"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
ext=".pdf"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
#plt.show()



# find cummulative data and plot it
ncum=[]
newtotal=0 
for i in range(len(simplehist)):
    newtotal=newtotal+simplehist[i]
    ncum.append(newtotal) 

plt.figure() # start a new plot and give it an number, starts from 0 and increments otherwise
ax = plt.subplot(111) # seems to create a 1 by 1 grid in figure 1 but it gives you access to the axes
ax.set_xscale('log')
ax.set_yscale('log')
plt.plot(simplebincentres,ncum,'x',color='black')

plt.xlabel('$k$', fontsize=fs)
plt.ylabel(r'$p_<(k)$', fontsize=fs)
plt.title(datatitle, fontsize=fs)

#plt.legend()

filenamewext=filenameroot+"ddcummulative"

ext=".eps"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
ext=".pdf"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
#plt.show()

# ******************************************************
# zipf plot
degreelist.sort(reverse=True) # note this changes the degreelist to be sorted

fig1= plt.figure() # start a new plot and give it an number, starts from 0 and increments otherwise
ax = plt.subplot(111) # seems to create a 1 by 1 grid in figure 1 but it gives you access to the axes
ax.set_xscale('log')
ax.set_yscale('log')

plt.plot(range(1,len(degreelist)+1),degreelist,'x',color='black')
plt.xlabel('rank', fontsize=fs)
plt.ylabel(r'$k$', fontsize=fs)
plt.title(datatitle, fontsize=fs)

#plt.legend()

filenamewext=filenameroot+"ddzipf"

ext=".eps"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
ext=".pdf"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
ext=".png"
filename=filenamewext+ext
plotfilename=os.path.join(outputdir,filename)
plt.savefig(plotfilename)
#plt.show()
