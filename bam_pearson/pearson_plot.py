#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:16:26 2017

@author: Nicholas
"""

# pearson plot generator
# python pearson_plot.py input.csv
#input:  csv file formatted chr:xxxxxxxx:yyyyyyyy,count1percentAlignedBases,count2percentAlignedBases
#output: pearson correlation png figure of count1 vs count2
# optional usage of either sys or manual input of file name

import matplotlib.pyplot as plt
import csv
import scipy.stats as sp
import numpy as np
import sys

def main():
 
    file1=sys.argv[1]	#command line functionality
    #file1='BAM.csv' 	#manual input of file
    
    fileName = file1.split('_')[0]    
    file = open(file1,'r')     #import csv file
    pearson_csv = csv.reader(file) 		#input csv
    next(pearson_csv) 				#skips header line
    
    #retrieve values
    regions = []
    count1 = []
    count2 = []
    for row in file:    #separate data
        line = row.split(",")
        regions.append(line[0])
        count1.append(int(line[1]))
        count2.append(int(line[2].rstrip()))
        
    pvalue = sp.pearsonr(count1,count2)     #pearsonr coefficient
    #print(pvalue) check pvalue
    
        
#    count1 = [i for i in count1 if i<22000] # filters outlier points
#    count2 = [i for i in count2 if i<10000] # needs optimizing 

    
    #Plots Figure
    if len(count1)==len(count2):
        plt.scatter(count1,count2,0.5,'k') #scatters points on graph
        plt.title(fileName+' Correlation') 
        plt.xlabel('File1: # of %Aligned Bases')
        plt.ylabel('File2: # of %Aligned Bases')
        plt.plot(np.unique(count1), np.poly1d(np.polyfit(count1, count2, 1))(np.unique(count1)),'r') #displays line of best fit
    
        #display pearson coeff
        plt.text(3000,1250,'pearsonr coefficient='+ str(pvalue[0])) 


        axes = plt.gca()
        #axes.set_xlim([0,max(count1)]) #set limit as max value of count
        #axes.set_ylim([0,max(count2)])  
        axes.set_xlim([0,7500])		#manually set limit
        axes.set_ylim([0,7500])

        plt.savefig(fileName+'_pearson.png') #creates save file
        plt.show() #displays graph
    else:
        print("# x data points="+str(len(count1)))
        print("# y data points="+str(len(count2)))
        print("Not the same number of x and y data points")
main()
