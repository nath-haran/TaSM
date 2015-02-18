import random 
from scipy import stats
import csv
import numpy as np
import pandas as pd
import simplejson
from math import sqrt
import itertools
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
rating_dict_product={}
set_userid=set([])
set_productid=set([])
rating_dict_product={}
ranges=[]
#rating_dict_product_users={}
def distance(item1,item2):
	sum_xy=0
	sum_x=0
	sum_y=0
	sum_x2=0
	sum_y2=0
	x=0
	y=0
	n=1
	for i in item2:
		if item2[i]!='':
			x=0
			y=0
			x=float(item1[list(set_userid).index(i)])
			y=float(item2[i])
			n=n+1
			sum_xy += x * y
			sum_x += x
			sum_y += y
			sum_x2 += x**2
			sum_y2 += y**2
	denominator = sqrt(sum_x2 - (sum_x**2) / n) *sqrt(sum_y2 -(sum_y**2) / n)
	if denominator == 0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y) / n) / denominator
list1=[]
def min(user):
	min1 = float(6.0)
	for product in rating_dict_product:
		if(rating_dict_product[product].has_key(user) and rating_dict_product[product][user]!=''):
			#print rating_dict_product[product][user]
			rating=float(rating_dict_product[product][user])
			if rating<min1:
				#print rating
				min1=rating
	if min1==6.0:
		return 0.0
	if min1=='':
		return 0.0
	return float(min1);

def max(user):
	max1 = float(0.0)
	for product in rating_dict_product:
		if(rating_dict_product[product].has_key(user) and rating_dict_product[product][user]!=''):
			#print rating_dict_product[product][user]
			rating=float(rating_dict_product[product][user])
			if rating>max1:
				#print rating
				max1=rating
	if max1==0.0 or max1=='':
		return 0.0
	return float(max1);



for row in reader:
	list1.append(dict(zip(header,row)))
#list_id=[]
header2=['userId','productId','rating']
list2=[]
for item in list1:
	if item['review/userId']!='unknown' and item['review/userId']!='':
		list2.append(dict(zip(header2,[item['review/userId'],item['product/productId'],item['review/score']])))
#for item in list2:
#	print list2
set_userid=set([])
set_productid=set([])
for item in list2:
	set_userid.add(item['userId'])
	set_productid.add(item['productId'])
for item in set_productid:
	rating_dict_product[item]={}
#for item in set_userid:
#	rating_dict_product_users[item]={}
k=10

for item in list2:
	rating_dict_product[item['productId']].update({item['userId'] : item['rating']})
ranges=[]
for user in set_userid:
	max1=max(user)
	min1=min(user)
	if(min1==''):
		min1=0.0
	if(max1==''):
		max1=0.0
	ranges.append((float(min1),float(max1)))
# for i in range(len(set_userid)):
#  	print ranges[i][0]
# for item in ranges:
#  	print item[1]


#clusters=[[random.random()*(float(ranges[i][1])-float(ranges[i][0]))+float(ranges[i][0]) for i in range(len(set_userid))] for j in range(10)]
#for item in clusters:
#	print item
clusters=[]
for i in range(k):
	clusters.append([])
k=5
lastmatches=None
for j in range(k):
	item=0
	for item in ranges:
		val1=item[1]-item[0]
		val2=val1+item[0]
		val3=random.random()*val2
		clusters[j].append(val3)
z=0
list_userid=list(set_userid)
list_productid=list(set_productid)
for t in range(5):
	print t
	bestmatches=[[] for i in range(k)]
	for row in rating_dict_product:
		bestmatch=0
		for i in range(k):
			d=distance(clusters[i],rating_dict_product[row])
			if d > distance(clusters[bestmatch],rating_dict_product[row]): bestmatch=i
			#print "bestmatches"
		bestmatches[bestmatch].append(row)
		print "skdjfh"+str(z)
		z+=1
	if bestmatches==lastmatches:
		break
	lastmatches=bestmatches
	for i in range(k):
	 avgs=[0.0]*len(set_userid)
	 if len(bestmatches[i])>0:
	 	m=0
	 	for productid in bestmatches[i]:
	 		m=0
	 		for userid in rating_dict_product[productid]:
	 		 m=list_userid.index(userid)
	 		 if rating_dict_product[productid][userid]!='':
			 	avgs[m]+=float(rating_dict_product[productid][userid])
	 	for j in range(len(avgs)):
	 		avgs[j]/=len(bestmatches[i])
	 	clusters[i]=avgs
writer=csv.writer(open("products_cluster.csv","wb"),quoting=csv.QUOTE_ALL)
for val in itertools.izip_longest(bestmatches[0],bestmatches[1],bestmatches[2],bestmatches[3],bestmatches[4],fillvalue=' '):
	writer.writerow(val)
	

	#rating_dict_product[item['userId']][item['productId']]=item['rating']

# for user in set_userid:
# 	if user!=cur_user:
# 		distance=0
# 		distance=pearson(cur_user,user)
# 		distance_list.append({'name': user,'distance':distance})
# sorted_distance_list=sorted(distance_list,key= lambda k : k['distance'],reverse=True)	