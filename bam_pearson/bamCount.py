#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:26:59 2017

@author: Nicholas
"""

# SAM reader


import pysam
import csv
import scipy.stats as sp
import matplotlib.pyplot as plt
 
def percentTargetAlignedBases(samfile, dic_bed):
    str(dic_bed)
    score = samfile.count(region = dic_bed)  #chr1:10000:20000
    return score
 
    

count1 = []
count2 = []


 
dic_bed={"chr1":249250621, 
         "chr2":243199373,
         "chr3":198022430,
         "chr4":191154276,
         "chr5":180915260,
         "chr6":171115067,
         "chr7":159138663,
         "chrX":155270560,
         "chr8":146364022,
         "chr9":141213431,
         "chr10":135534747,
         "chr11":135006516,
         "chr12":133851895,
         "chr13":115169878,
         "chr14":107349540,
         "chr15":102531392,
         "chr16":90354753,
         "chr17":81195210,
         "chr18":78077248,
         "chr20":63025520,
         "chrY" :59373566,
         "chr19":59128983,
         "chr22":51304566,
         "chr21":48129895,
         "chrM" :16571
         }

samfile = pysam.AlignmentFile("test1.bam","rb",check_sq=False)   #input bam
samfile2 = pysam.AlignmentFile("test1.bam","rb",check_sq=False)
#samfile = input("Please input the name of the 1st bam file: ",'rb')
#samfile2 = input("Please input the name of the 2nd bam file: ",'rb')

#size = input("Please input desired bin size: ")   #create bins
size = 10000
bin_size=size
regions=[]
for CHR in dic_bed:
    bin_number=int(dic_bed[CHR])/int(bin_size)
    for i in range(0,round(bin_number)):
        start=str(i*bin_size+1)
        end=str((i+1)*bin_size)
        input_range=CHR+":"+start+":"+end
        regions.append(input_range)
        
        
for entry in regions:
    score = percentTargetAlignedBases(samfile,entry)
    count1.append(score)   
    
for entry in regions:
    score = percentTargetAlignedBases(samfile2,entry)
    count2.append(score)      
    
#filter repeated zeros
sections = [regions[x] for x in range(len(regions)) if count1[x]!=0 or count2[x]!=0]
lst1 = [count1[x] for x in range(len(regions)) if count1[x]!=0 or count2[x]!=0]
lst2 = [count2[x] for x in range(len(regions)) if count1[x]!=0 or count2[x]!=0]
count1 = lst1
count2 = lst2
regions = sections
    
pvalue = sp.pearsonr(count1,count2)     #pearsonr coefficient
print(pvalue)

outfile = open('BAM.csv','w')   #output csv
writer = csv.writer(outfile)
writer.writerow(['regions','count1','count2'])


for i in range(len(regions)):
    writer.writerow([regions[i],count1[i],count2[i]])    
outfile.close
  

    
plt.scatter(count1,count2)    #generate scatterplot of data
plt.title('Correlation') 
plt.xlabel('File 1')
plt.ylabel('File 2')   


outfile.close
