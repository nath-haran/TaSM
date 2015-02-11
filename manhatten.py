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
#for item in list2:
#	print list2
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
	#rating_dict[item['userId']][item['productId']]=item['rating']
cur_user='A2D1LPEUCTNT8X'
for user in set_userid:
	if user!=cur_user:
		distance=0
		for item in set_productid:
			d1=0.0
			d2=0.0
			if rating_dict[cur_user].has_key(item) and rating_dict[cur_user][item]!='':
				#print rating_dict[cur_user][item]
				d1=float(rating_dict[cur_user][item])
			if rating_dict[user].has_key(item) and rating_dict[user][item]!='':
				#print rating_dict[user][item]
				d2=float(rating_dict[user][item])
			distance=distance+abs(d1*d1 - d2*d2)
	distance_list.append({'name': user,'distance':distance})
	#distance_list[user]=np.sqrt(distance)'
	#distance_list.sort()
	sorted_distance_list=sorted(distance_list,key= lambda k : k['distance'])

for item in sorted_distance_list:
	print str(item['name'])+":"+str(item['distance'])
	#print item+":"+str(distance_list[item])
#for item in rating_dict:
#	print simplejson.dumps(rating_dict[item])



#print set_userid


#array_id=np.array(list_id)
#Array_id=np.array([])
#i=0
#for item in array_id:
#	if item=='unknown':
		#print item
#		Array_id=np.delete(array_id,i)
#	i=i+1
#for item in array_id:
#	print item
	

#print stats.mode(array_id,axis=None)
