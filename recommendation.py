from scipy import stats
import csv
import numpy as np
import pandas as pd
import simplejson
distance_list=[]
#building dictionary
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
#for item in list2:
#	print list2
set_userid=set([])
set_productid=set([])
for item in list2:
	set_userid.add(item['userId'])
	set_productid.add(item['productId'])
rating_dict={}
for item in set_userid:
	rating_dict[item]=[]
i=0
distance_list=[]
for item in list2:
	rating_dict[item['userId']].append(item['productId'])
#end dictionary build


f=open('output.txt','r')
i=0
for l in f:
	if i<100:
		(user,distance)=l.split(':')
		distance_list.append(user) #update in ipython 
		i=i+1
recommendations=set([])
user_dict=rating_dict['A2D1LPEUCTNT8X']
for user in distance_list:
	for product in rating_dict[user]:
#if not product in user_dict:
		recommendations.add(product)
for item in recommendations:
	print item


