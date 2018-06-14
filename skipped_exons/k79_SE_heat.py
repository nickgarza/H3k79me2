
import sys
import csv
import pysam

def dictionaryBED(line_file, i):
        dic_BED=[]
        col=line_file.split(":")
        bed_range = [col[0],str(int(col[i])-50),str(int(col[i]))]
        dic_BED=":".join(bed_range)
        #print(dic_BED)
        return dic_BED

def dictionaryBED_down(line_file, i):
        dic_BED_down=[]
        col=line_file.split(":")
        bed_range = [col[0],str(int(col[i])),str(int(col[i])+50)]
        dic_BED_down=":".join(bed_range)
        return dic_BED_down


def percentTargetAlignedBases(samfile, dic_bed):
        pile_dic={}
        start = int(dic_bed.split(":")[1])
        end = int(dic_bed.split(":")[2])
        for pileupcolumn in samfile.pileup(region = dic_bed):  #chr1:10000:20000
                pile_dic[pileupcolumn.pos]=pileupcolumn.n
        for base_pos in range(start, end):
                        #print(base_pos,start,end)
                if base_pos in pile_dic.keys():
                        print(pile_dic[base_pos])#,end=",")
                else:
                        print("0")#,end=",")


Bed_file = sys.argv[1]
bam_file = sys.argv[2]
samfile = pysam.AlignmentFile(bam_file, "rb")
bed_file= open(Bed_file)
for line in bed_file:
        #temp=aaa.split("\t")[2:]
        #line="\t".join(temp)
        xxx=line.split(":")
        if xxx[9]=="+":
                dic_BED1=dictionaryBED(line,2)
                dic_BED2=dictionaryBED_down(line,2)
                dic_BED3=dictionaryBED(line,4)
                dic_BED4=dictionaryBED_down(line,4)
                dic_BED5=dictionaryBED(line,5)
                dic_BED6=dictionaryBED_down(line,5)
                dic_BED7=dictionaryBED(line,7)
                dic_BED8=dictionaryBED_down(line,7)
        else:
                dic_BED1=dictionaryBED_down(line,1)
                dic_BED2=dictionaryBED(line,1)
                dic_BED3=dictionaryBED_down(line,6)
                dic_BED4=dictionaryBED(line,6)
                dic_BED5=dictionaryBED_down(line,5)
                dic_BED6=dictionaryBED(line,5)
                dic_BED7=dictionaryBED_down(line,10)
                dic_BED8=dictionaryBED(line,10)
        percentTargetAlignedBases(samfile, dic_BED1)
        percentTargetAlignedBases(samfile, dic_BED2)
        percentTargetAlignedBases(samfile, dic_BED3)
        percentTargetAlignedBases(samfile, dic_BED4)
        percentTargetAlignedBases(samfile, dic_BED5)
        percentTargetAlignedBases(samfile, dic_BED6)
        percentTargetAlignedBases(samfile, dic_BED7)
        percentTargetAlignedBases(samfile, dic_BED8)
        print("")
        #break

