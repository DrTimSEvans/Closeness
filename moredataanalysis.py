'''
Plots and Analysis MoreDAtaSets files for closeness paper
@author: time
'''

import math

# Useful for manipulating filenames without worrying about which OS you use
import os

# Useful for many things
import numpy as np

import pandas as pd

# Plot library produces excellent high quality plots and emulates MatLab (which may or may not be of use to you)
# I would think of using python/matplotlib for plotting even if you do your sums in another language
# for plot tutorial see http://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

import matplotlib as mpl

# see http://matplotlib.org/api/pyplot_api.html
# fontsize in points try 12 for a4 paper 18 or 24 for overheads
fs=15
# plot marker size in pts, use as markersize=ms
ms=10


def saveFigure(plt,filenameroot,extlist=['pdf'],messageString='Plot',screenOn=False):
    '''Save figure as file
    
    Input
    plt -- plot to be save
    filenameroot -- full name of file excpet for extension
    extlist=['pdf'] -- list of extensions to be used
    messageString='Plot' -- message to print out, none if empty string
    '''
    for ext in extlist:
        if filenameroot.endswith('.'):
            plotfilename=filenameroot+ext
        else:
            plotfilename=filenameroot+'.'+ext
        if len(messageString)>0:
            print (messageString+' file '+plotfilename)
        plt.savefig(plotfilename)
    if screenOn:
        plt.show()



if __name__ == '__main__':

    """
    I find that UNIX style forward slashes work on any OS in most languages
     They should be backwards slashes on Windows but a backwards slash has a special meaning
     so I recommend just using a forwards slash where a backwards would be used on Windows
     This is the directory where I want my outputs to go
     MAKE SURE DIRECTORY EXISTS!
     outputdir='h:/CandN/output/"
    """
    outputdir="D:/DATA/Closeness/output/"
    inputdir="./input/"
    filenameroot="MoreDataSets220127"


    # ***********************************************************

    fullinputfilename=os.path.join(inputdir,filenameroot+".dat")
    print ('--- Reading network analysis data from ',fullinputfilename)

    df = pd.read_csv(fullinputfilename,sep='\t')

    print(df.columns.values)
    
    Npdlabel = 'N_vv' 
    Nlabel = 'N' 
    kavpdlabel = '<k>' 
    kavlabel = r'$\langle k \rangle$' 
    rhopdlabel = 'rho'
    rholabel = r'$\rho$'
    chirpdlabel = 'reduced-chi'
    chirlabel = r'$\chi_r$'
    
    xpdlabel = Npdlabel
    ypdlabel = chirpdlabel
    xlabel = Nlabel
    ylabel = chirlabel

    xvalues = df[xpdlabel]
    yvalues = df[ypdlabel]
    crholist = [ ]
    mrholist = [ ]
    for rho in df[rhopdlabel]:
        if rho>0.1:
            m = 'o'
            c = 'r'
        elif rho>0.01:
            m = 'g'
            s = 's'
        else:
            m= 'b'
            s = '^'
        crholist.append(c)
        mrholist.append(s)
            
#    COLOUR_LIST = ['b', 'r', 'g', 'm', 'c', 'y', 'k']
#    SHAPE_LIST  = ['o', '^', 's', 'D', 'x', 'h', '*']

    
    #subtitle_string=r"abc"
    #plt.suptitle(subtitle_string)
    
    # Plot reduced chi vs N with  rho as colorbar
    
    fig1, ax1 = plt.subplots()
    ax1.set_ylabel(ylabel)
    ax1.set_xlabel(xlabel)
    ax1.set_ylim([0.1, 100])
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    #plt.axes().set_aspect('equal')
    dfrange1 = (df[rhopdlabel]>0.1)
    #print (dfrange1)
    clist1=df.loc[dfrange1,[rhopdlabel]]
    # For normalisation see
    # see https://matplotlib.org/stable/tutorials/colors/colormapnorms.html
    normrho = mpl.colors.Normalize(vmin=0, vmax=1.0)
    cmaprho='viridis_r'
    ax1.scatter(df.loc[dfrange1, [Npdlabel] ], 
                df.loc[dfrange1, [chirpdlabel] ],
                marker='^',
                c=clist1[rhopdlabel].tolist(), 
                norm = normrho,
                cmap=cmaprho,
                edgecolors='k')
    dfrange2 = ((df[rhopdlabel]<=0.1) & (df[rhopdlabel]>0.01))
    clist2=df.loc[dfrange2,[rhopdlabel]]
    ax1.scatter(df.loc[ dfrange2 ,[Npdlabel] ],
                df.loc[ dfrange2 ,[chirpdlabel]],
                marker='s',
                c=clist2[rhopdlabel].tolist(), 
                norm = normrho,
                cmap=cmaprho,
                edgecolors='k')
    dfrange3 = (df[rhopdlabel]<=0.01) 
    clist3=df.loc[dfrange3,[rhopdlabel]]
    ax1.scatter(df.loc[ dfrange3 ,[Npdlabel] ],
                df.loc[ dfrange3 ,[chirpdlabel]],
                marker='o',
                c=clist3[rhopdlabel].tolist(), 
                norm = normrho,
                cmap=cmap1,
                edgecolors='k')
    #https://matplotlib.org/stable/tutorials/colors/colorbar_only.html
    cbar1 = fig1.colorbar(mpl.cm.ScalarMappable(norm=normrho, cmap=cmaprho))
    cbar1.ax.set_ylabel(rholabel)
    
    #plt.show()
    plotfilenameroot=os.path.join(outputdir,filenameroot+"_N_chir_rho.dat")   
    saveFigure(plt,plotfilenameroot,extlist=['pdf','svg'],messageString='Plot',screenOn=False)


    # Plot reduced chi vs N with  <k> as colorbar
    
    fig2, ax2 = plt.subplots()
    ax2.set_ylabel(ylabel)
    ax2.set_xlabel(xlabel)
    ax2.set_ylim([0.1, 100])
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    #plt.axes().set_aspect('equal')
    dfrange2 = (df[kavpdlabel]>0.1)
    #print (dfrange1)
    clist2=df.loc[dfrange2,[kavpdlabel]]
    # For normalisation see
    # see https://matplotlib.org/stable/tutorials/colors/colormapnorms.html
    normkav = mpl.colors.Normalize(vmin=1, vmax=100.0)
    cmap2='viridis_r'
    ax2.scatter(df.loc[dfrange2, [Npdlabel] ], 
                df.loc[dfrange2, [chirpdlabel] ],
                marker='^',
                c=clist2[kavpdlabel].tolist(), 
                norm = normkav,
                cmap=cmap2,
                edgecolors='k')
    dfrange2 = ((df[kavpdlabel]<=0.1) & (df[kavpdlabel]>0.01))
    clist2=df.loc[dfrange2,[kavpdlabel]]
    ax2.scatter(df.loc[ dfrange2 ,[Npdlabel] ],
                df.loc[ dfrange2 ,[chirpdlabel]],
                marker='s',
                c=clist2[kavpdlabel].tolist(), 
                norm = normkav,
                cmap=cmap2,
                edgecolors='k')
    dfrange3 = (df[kavpdlabel]<=0.01) 
    clist3=df.loc[dfrange3,[kavpdlabel]]
    ax2.scatter(df.loc[ dfrange3 ,[Npdlabel] ],
                df.loc[ dfrange3 ,[chirpdlabel]],
                marker='o',
                c=clist2[kavpdlabel].tolist(), 
                norm = normkav,
                cmap=cmap2,
                edgecolors='k')
    #https://matplotlib.org/stable/tutorials/colors/colorbar_only.html
    cbar2 = fig2.colorbar(mpl.cm.ScalarMappable(norm=normkav, cmap=cmap2))
    cbar2.ax.set_ylabel(kavlabel)
    
    #plt.show()
    plotfilenameroot=os.path.join(outputdir,filenameroot+"_N_chir_kav.dat")   
    saveFigure(plt,plotfilenameroot,extlist=['pdf','svg'],messageString='Plot',screenOn=False)

    # Plot reduced chi vs <k>  with rho as colorbar

    xpdlabel = kavpdlabel
    xlabel = kavlabel

    
    fig3, ax3 = plt.subplots()
    ax3.set_ylabel(ylabel)
    ax3.set_xlabel(xlabel)
    ax3.set_ylim([0.1, 100])
    ax3.set_xscale("log")
    ax3.set_yscale("log")
    #plt.axes().set_aspect('equal')
    dfrange1 = (df[rhopdlabel]>0.1)
    #print (dfrange1)
    clist3=df.loc[dfrange1,[rhopdlabel]]
    # For normalisation see
    # see https://matplotlib.org/stable/tutorials/colors/colormapnorms.html
    #normrho = mpl.colors.Normalize(vmin=0, vmax=1.0)
    #cmap1='viridis_r'
    ax3.scatter(df.loc[dfrange1, [Npdlabel] ], 
                df.loc[dfrange1, [chirpdlabel] ],
                marker='^',
                c=clist1[rhopdlabel].tolist(), 
                norm = normrho,
                cmap=cmaprho,
                edgecolors='k')
    dfrange2 = ((df[rhopdlabel]<=0.1) & (df[rhopdlabel]>0.01))
    clist2=df.loc[dfrange2,[rhopdlabel]]
    ax3.scatter(df.loc[ dfrange2 ,[Npdlabel] ],
                df.loc[ dfrange2 ,[chirpdlabel]],
                marker='s',
                c=clist2[rhopdlabel].tolist(), 
                norm = normrho,
                cmap=cmaprho,
                edgecolors='k')
    dfrange3 = (df[rhopdlabel]<=0.01) 
    clist3=df.loc[dfrange3,[rhopdlabel]]
    ax3.scatter(df.loc[ dfrange3 ,[Npdlabel] ],
                df.loc[ dfrange3 ,[chirpdlabel]],
                marker='o',
                c=clist3[rhopdlabel].tolist(), 
                norm = normrho,
                cmap=cmaprho,
                edgecolors='k')
    #https://matplotlib.org/stable/tutorials/colors/colorbar_only.html
    cbar3 = fig3.colorbar(mpl.cm.ScalarMappable(norm=normrho, cmap=cmaprho))
    cbar3.ax.set_ylabel(rholabel)
    
    #plt.show()
    plotfilenameroot=os.path.join(outputdir,filenameroot+"_Nkav_chir_rho.dat")   
    saveFigure(plt,plotfilenameroot,extlist=['pdf','svg'],messageString='Plot',screenOn=False)






#    plt.ylabel(ylabel)
#    plt.xlabel(xlabel)
#    plt.ylim([0.1, 100])
#    plt.xscale("log")
#    plt.yscale("log")
#    #plt.axes().set_aspect('equal')
#    plt.scatter(df.loc[df[rhopdlabel]>0.1,[xpdlabel]],df.loc[df[rhopdlabel]>0.1,[chirpdlabel]],marker='o',color='r')
#    plt.scatter(df.loc[(df[rhopdlabel]<=0.1) & (df[rhopdlabel]>0.01)  ,[xpdlabel] ],df.loc[(df[rhopdlabel]<=0.1) & (df[rhopdlabel]>0.01),[chirpdlabel]],marker='s',color='b')
#    plt.scatter(df.loc[ df[rhopdlabel]<=0.01  ,[xpdlabel] ],df.loc[ df[rhopdlabel]<=0.01,[chirpdlabel]],marker='^',color='g')
#    plt.show()

    #print (df.loc[df[rhopdlabel]>0.1,[Npdlabel]])