import csv
import gzip
import simplejson
import scipy,numpy,pandas
reader=open("output.txt","r")
i=0
for l in reader:
  if l.strip()==="A2D1LPEUCTNT8X":
    print l
print i
