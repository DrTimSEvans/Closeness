import getpass
import math
import matplotlib.pyplot as plt

import ast

#import networkx as nx
#import numpy as np
#import os
#import pandas as pd
#try:
#    import cPickle as pickle
#except:
#    import pickle
#import random as rn
#import re
#import scipy as sp
#from sets import Set
#import time


class TimUtilities:
    '''
    Various useful utilities and values
    '''
    
    GRAPHIC_FILE_SUFFIX_LIST = ['.png', '.pdf', '.eps']
    COLOUR_LIST = ['b', 'r', 'g', 'm', 'c', 'y', 'k']
    SHAPE_LIST  = ['o', '^', 's', 'D', 'x', 'h', '*']
    MARKER_LIST = [] #[COLOUR_LIST[x] + SHAPE_LIST[x] for x in range(len(COLOUR_LIST))]
    CURVE_LIST = [] #[x + '-' for x in COLOUR_LIST]

    DATA = 'Unknown'
    RESULTS = 'Unknown'
    USERNAME = 'Unknown'

    def __init__(self):
        #self.GRAPHIC_FILE_SUFFIX_LIST = TimUtilities.get_graphics_file_suffixes()
        #self.COLOUR_LIST,  self.SHAPE_LIST, self.MARKER_LIST, self.CURVE_LIST = TimUtilities.get_matplotlib_features()
        self.DATA, self.RESULTS, self.USERNAME = TimUtilities.setDirectories()
        self.MARKER_LIST, self.CURVE_LIST = get_matplotlib_features()

        # put filepaths to data and models on each machine we use here
        print ('-- user {0:s}'.format(self.USERNAME))
        print ('-- User is %s' % self.USERNAME    )    
        print ('-- DEBUGON is %s' % self.DEBUGON )
        print ('-- DATA input from %s' % self.DATA)
        print ('-- RESULTS output to %s' % self.RESULTS)


        

    
    @staticmethod
    def saveFigure(self,plt,filenameroot,extlist=['pdf'],messageString='Plot',screenOn=False):
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

    def setDirectories(self):
        self.DATA, self.RESULTS, self.USERNAME = TimUtilities.findLocations()

    @staticmethod
    def findLocations():
        '''
        Finds appropriate strings for input directory (DATA), output (RESULTS) directory and the username (USERNAME)
        
        Output
        Sets the following global values
        DATA - the directory with input data
        RESULTS - the directory with output data
    
        Return
        DATA,RESULTS
        '''
        USERNAME = getpass.getuser()
        if USERNAME == 'jrc309':
            # James CMTH machine
            DATA = '/data/users/jrc309/DAG/Data/'
            RESULTS = '/data/users/jrc309/DAG/Results/'
        elif USERNAME == 'james':
            # James home machine
            DATA = "/home/james/HDD/DATA/DAG/DAG_DATA/"
            RESULTS = "/home/james/HDD/DATA/DAG/DAG_RESULTS"
        elif USERNAME == 'time' :
            # Tim Imperial machine
            DATA = 'c:/DATA/DAG/input/'
            RESULTS = 'c:/DATA/DAG/output/'    
        elif USERNAME == 'TEvan_000':
            # Tim Imperial machine
            DATA = 'G:/DATA/DAG/input/'
            RESULTS = 'G:/DATA/DAG/output/'    
        elif USERNAME == 'tseva':
            # Tim Imperial machine
            DATA = 'd:/DATA/DAG/input/'
            RESULTS = 'd:/DATA/DAG/output/'    
        else:
            print ('*** Unknown user {0:s} - things might not work since dagology does not know where to find data or put results'.format(USERNAME))
            import os
            print ('*** so using current working directory '+os.getcwd())        
            DATA = os.getcwd() #'Unknown'
            RESULTS = os.getcwd() #'Unknown'
        return DATA,RESULTS, USERNAME
    
    
    
#     @staticmethod
#     def get_graphics_file_suffixes(self):
#         '''Simple list of suitbale graphics file suffixes
# 
#         '''
#         return ['.png', '.pdf', '.eps']
    
    def get_matplotlib_features(self):
        '''
        This uses the TimUtilities class globals
        TimUtilities.COLOUR_LIST = list of allowed colours
        TimUtilities.SHAPE_LIST = list of allowed shapes
        to define  
        marker_list =  list of allowed markers, each is two characters a colour then a marker symbol,
        curve_list =  list of allowed markers, each is three characters a colour then a marker symbol then a line symbol
         
        Return
        tuple of 
        marker_list, curve_list
        '''
        #COLOUR_LIST = ['b', 'r', 'g', 'm', 'c', 'y', 'k']
        #SHAPE_LIST = ['o', '^', 's', 'D', 'x', 'h', '*']
        marker_list  = [TimUtilities.COLOUR_LIST[x] + TimUtilities.SHAPE_LIST[x] for x in range(len(TimUtilities.COLOUR_LIST))]
        curve_list   = [x + '-' for x in TimUtilities.COLOUR_LIST]
        return marker_list, curve_list

    @staticmethod
    def get_matplotlib_features():
        '''
        Return the gloabls
        tuple of 
        COLOUR_LIST, SHAPE_LIST, MARKER_LIST, CURVE_LIST
        '''
        
        return TimUtilities.COLOUR_LIST, TimUtilities.SHAPE_LIST, TimUtilities.MARKER_LIST, TimUtilities.CURVE_LIST





    @staticmethod
    def get_colour_scheme(self):
        '''NICE COLOUR SCHEMES
        
        Return
        List of 20 nice colours suitable for matplotlib
        '''        
        tableau20 = [(31, 119, 180), (214, 39, 40), (44, 160, 44), (255, 127, 14),   
                     (174, 199, 232), (152, 223, 138),  (255, 152, 150), (255, 187, 120),
                     (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),  
                     (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),  
                     (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  
          
        # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.  
        for i in range(len(tableau20)):  
            r, g, b = tableau20[i]  
            tableau20[i] = (r / 255., g / 255., b / 255.) 
        return tableau20
    
    @staticmethod        
    def read_blog_info(postDataFile):
        '''Read in data from the Vaiva post data file
        
        This input file is usually the postData.txt produced by Vaiva.
        The format of the file is for each post we have a line containing
        <post_id>::{<dictionary_data>} 
        Full information is in the OneNote page "Information on postData.txt" but
        the following is a list of expected keys
         key    description of value
        'posted on'    date in UNIX format? Correct
        'url'    the url of the blog post, presumably in one-to-one match
                 with blog id? No. In my opinion, this is a permanent url link to the post in the blog. So If the url of a blog is "blog.com", then this url is "blog.com/post_name" . Blog ID however is an integer, unrelated to the name of a blog (some internal enumeration).
        'feed_id'    presumably a unique number for the blog
        'links'    A list of links. So square brackets surround a comma separated list of urls given as strings in single quotes. You could use ast.literal_eval(your_list) and this will be converted into a list. These are all url links found in the blog post.
        'categories'    User generated keyword phrases? Square brackets surround a comma separated list strings in single quotes. These were provided by Altmetrics.

        The result is postData, a dictionary of dictionaries where
        for an integer post_id we have postData[post_id] as a dictionary.
        
        
        Input
        postDataFile - name of input Vaiva style text file of data on posts
        
        Return
        postData - dictionary of dictionaries, postData[post_id]
        '''
        #obtain post info from file
        postData={}
        with open(postDataFile,"rb") as f:
            for line in f:
                key,val = line.decode("utf-8").split("::",1)
                # note https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
                # explains that ast.literal_eval willl evaluate a string as a Python expression
                postData[int(key)] = ast.literal_eval(val.rstrip())
