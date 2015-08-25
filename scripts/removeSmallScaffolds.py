#!/bin/env python

#removeSmallScaffolds.py

#Take 3 arguments: input file, base name for output, and cutoff value. 
#Returns a file named output_clipped.fasta with all the scaffolds >= cutoff.

import sys

outName=sys.argv[2]
file=sys.argv[1]
cutoff=sys.argv[3]
alignment=open(file,"r")
output=open(outName+"_clipped.fasta","w")

toWrite=''
for line in alignment:
    if '>' in line:
        if len(toWrite) >= cutoff:
            output.write(toWrite)
        toWrite=str(line)+'\n'
        current=str(line)
    else:
        toWrite+=str(line)+'\n'
output.close()