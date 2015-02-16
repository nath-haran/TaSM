from operator import itemgetter
from scipy import stats
import csv
import numpy as np
import pandas as pd
import simplejson
reader=csv.reader(open("arts.csv","r"))
header=reader.next()

list1=[]
for row in reader:

	list1.append(dict(zip(header,row)))
#list_id=[]
header2=['userId','productId','rating']
list2=[]
for item in list1:
	if item['review/userId']!='unknown':
		list2.append(dict(zip(header2,[item['review/userId'],item['product/productId'],item['review/score']])))
set_userid=set([])
set_productid=set([])
for item in list2:
	set_userid.add(item['userId'])
	set_productid.add(item['productId'])
rating_dict={}
for item in set_userid:
	rating_dict[item]={}
i=0
distance_list=[]
for item in list2:
	rating_dict[item['userId']].update({item['productId'] : item['rating']})
list_count=[]
for item in set_userid:
	list_count.append({'user':item,'count':len(rating_dict[item])})
from operator import itemgetter
newlist = sorted(list_count, key=itemgetter('count'),reverse=True) 
for i in range(10):
	print newlist[i]['user']