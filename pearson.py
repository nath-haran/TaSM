from scipy import stats
import csv
import numpy as np
import pandas as pd
import simplejson
from math import sqrt
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
rating_dict={}
set_userid=set([])
set_productid=set([])
def pearson(user1,user2):
	sum_xy=0
	sum_x=0
	sum_y=0
	sum_x2=0
	sum_y2=0
	x=0
	y=0
	n=0
	for product in set_productid:
		if rating_dict[user1].has_key(product) and rating_dict[user1][product]!='':
			#print rating_dict[cur_user][item]
			x=float(rating_dict[user1][product])
			
		
		if rating_dict[user2].has_key(product) and rating_dict[user2][product]!='':
			#print rating_dict[user][item]
			y=float(rating_dict[user2][product])
		n=n+1
		sum_xy += x * y
		sum_x += x
		sum_y += y
		sum_x2 += x**2
		sum_y2 += y**2	
	
	#	if n==0:
	#		return 0
	denominator = sqrt(sum_x2 - (sum_x**2) / n) *sqrt(sum_y2 -(sum_y**2) / n)
	if denominator == 0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y) / n) / denominator
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

for item in list2:
	set_userid.add(item['userId'])
	set_productid.add(item['productId'])

for item in set_userid:
	rating_dict[item]={}
i=0
distance_list=[]
for item in list2:
	rating_dict[item['userId']].update({item['productId'] : item['rating']})
	#rating_dict[item['userId']][item['productId']]=item['rating']
cur_user='A2D1LPEUCTNT8X'
for user in set_userid:
	if user!=cur_user:
		distance=0
		distance=pearson(cur_user,user)
		distance_list.append({'name': user,'distance':distance})
sorted_distance_list=sorted(distance_list,key= lambda k : k['distance'],reverse=True)
#for item in sorted_distance_list:
	#print str(item['name'])+":"+str(item['distance'])
user_dict=rating_dict['A2D1LPEUCTNT8X']
i=0

recommendations=set([])
for item in distance_list:
	if i<90:
		for product in rating_dict[item['name']]:
#if not product in user_dict:
			recommendations.add(product)
	i+=1
for item in recommendations:
	print item
