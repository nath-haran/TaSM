from scipy import stats
import csv
import numpy as np
import pandas as pd
import simplejson
from math import sqrt
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
rating_dict_product={}
rating_dict_users={}
list1=[]

avg_rating={}
#implement adjusted cosine formula
def calculate_similarity(item1,item2):
	num=0
	num1=0
	num2=0
	den1=0
	den2=0
	for key1 in rating_dict_product[item1]:
		
		if rating_dict_product[item2].has_key(key1):
			avg=avg_rating[key1]
			
			num1=float(rating_dict_product[item2][key1])-float(avg)
			num2=float(rating_dict_product[item1][key1])-float(avg)
			#remove
			#print avg
			#print rating_dict_product[item2][key1]
			#print rating_dict_product[item1][key1]
			#print num1
			#print num2
			###
			num+=(num1)*(num2)
			#print num
			den1+=(num1)**2
			den2+=(num2)**2
			
	den=sqrt(den1)*sqrt(den2)
	#if num==0:
	#	return 0
	if den==0:
		return 0
	return num/(den)


###
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
for item in set_productid:
	rating_dict_product[item]={}
for item in set_userid:
	rating_dict_users[item]={}

for item in list2:
	rating_dict_product[item['productId']].update({item['userId'] : item['rating']})
for item in list2:
	rating_dict_users[item['userId']].update({item['productId'] : item['rating']})

for key in set_userid:
	avg_rating[key]={}
for user in rating_dict_users:
	summ=0
	count=0
	for key in rating_dict_users[user]:
		if rating_dict_users[user][key]!='' and rating_dict_users[user][key]!='unknown':
			summ+=float(rating_dict_users[user][key])
			count+=1
	if count!=0:
		avg_rating[user]=float(float(summ)/count)
	else:
		avg_rating[user]=0
i=0
j=0
length=len(set_productid)
distance_matrix=np.ndarray(shape=(length,length),dtype=float,order='F')
for item1 in set_productid:
	j=0
	for item2 in set_productid:
		similarity=0
		if item1!=item2:
			#similarity=float(0)
			similarity=calculate_similarity(item1,item2)
		distance_matrix[i][j]=similarity
		#if distance_matrix[i][j]!=0.0:
		#	print distance_matrix[i][j]
		j+=1
	i+=1
i=0
j=0

#for item1 in set_productid:
#	j=0
#	print item1+":"
#	for item2 in set_productid:
#		if distance_matrix[i][j]>0.0:
#			print item2
		#print item1+":"+item2+":"+str(distance_matrix[i][j])
#		j+=1
#	i+=1	
related_dict={}
for item in set_productid:
	related_dict[item]=[]
for item1 in set_productid:
	j=0
	for item2 in set_productid:
		if item1!=item2:
			if distance_matrix[i][j]>0.0:
				#print "entered"
				related_dict[item1].append(item2)
		j+=1
	i+=1
#f=open('related-items.csv')
#writer=csv.DictWriter(f,'w')
for row in related_dict:
	print str(row)+":",
	for item in related_dict[row]:
		print item,
	print ''
#f.close()

