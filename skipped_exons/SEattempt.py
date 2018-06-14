#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:56:21 2017

@author: Nicholas
"""
import pandas as pd
import math


class entry: # creates object for each entry
    
    def __init__(self,name,start,stop):
        self.name = name
        self.start = start
        self.stop = stop
        
    def getName(self):
        return str(self.name)
    
    def getStart(self):
        return int(self.start)
    
    def getStop(self):
        return int(self.stop)
    
    
 
def list_duplicates(seq): # generates list of indices of repeat values
    seen = set()
    seen_add = seen.add
    return [idx for idx,item in enumerate(seq) if item in seen or seen_add(item)]

def list_range_check(seq): # generates list of indices within range
    lst = []
    for item in seq:
        for entry in seq:
            if neighborhood(item,entry) and item!=entry:
                lst.append(seq.index(item))
    return lst



def neighborhood(one,two):
    if math.fabs(one - two)<=1000:
        return True
    return False    

def inter(seq1,seq2,seq3): # intersection of 3 sets
    lst = []
    for i in seq1:
        if i in seq2 or i in seq3: # chrm start OR stop repeated
            lst.append(i)
    return lst
    



    

def main():
    
    # initialize and open file
    infile = open("SE_compiled.txt",'r')
    lines = infile.readlines()
    
    reads = []
    col1 = []
    entries = []
    
    
    chrm = []
    start = []
    stop = []
    
    
    # splice file lines for name, start number and stop number
    for line in lines:
        
        reads = line.split()
        field = entry(reads[0], reads[1], reads[2])
        strng = reads[0] +"\t"+ str(reads[1]) +"\t"+ str(reads[2])
        
        col1.append(strng) # list to output info
        entries.append(field) # list of objects
        chrm.append(field.getName()) # list of chrm
        start.append(field.getStart()) # list of start numbers
        stop.append(field.getStop()) # list of stop numbers
        
    
#    print(entries[0].getStart())
    
# ------------------------------------
    # mark exact duplicates
    strand = [0]*len(start)

    

    repeatName = list_duplicates(chrm)
    repeatStart = list_duplicates(start)
    repeatStop = list_duplicates(stop)
    repeat = inter(repeatName,repeatStart,repeatStop) # repeated intervals on chrms
    print(len(repeat))
    for index in repeat:
        strand[index] = 1
    
    
#    # check within 1000 bp
#    checkName = list_duplicates(chrm)
#    checkStart = list_range_check(start)
#    checkStop = list_range_check(stop)
#    repeat = inter(checkName,checkStart, checkStop)
#    print(len(repeat))
#    for index in repeat:
#        strand[index] = 1

    

    
# -------------------------------------
    # output data to csv using pandas
    data = {'ID':col1, 'strand':strand}
    table = pd.DataFrame(data, columns = {'ID','strand'})
    
    out = open('SE_filtered.csv', 'w')
    table.to_csv(out)
    
  
    
    
    infile.close
    
    
    
        
main()

# in case need individual cols
 #   data = {'chrm': chrm,'start':start, 'stop': stop}
 #   table = pd.DataFrame(data, columns = {'chrm', 'start', 'stop'})