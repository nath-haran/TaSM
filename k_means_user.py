import itertools
import random 
import csv
from math import sqrt
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
set_userid=set([])
set_productid=set([])
rating_dict_user={}
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
			x=float(item1[list(set_productid).index(i)])
			#print x
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
def min(product):
	min1 = float(6.0)
	for user in rating_dict_user:
		if(rating_dict_user[user].has_key(product) and rating_dict_user[user][product]!=''):
			#print rating_dict_product[product][user]
			rating=float(rating_dict_user[user][product])
			if rating<min1:
				#print rating
				min1=rating
	if min1==6.0:
		return 0.0
	if min1=='':
		return 0.0
	return float(min1);

def max(product):
	max1 = float(0.0)
	for user in rating_dict_user:
		if(rating_dict_user[user].has_key(product) and rating_dict_user[user][product]!=''):
			#print rating_dict_product[product][user]
			rating=float(rating_dict_user[user][product])
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
	if item['review/userId']!='unknown':
		list2.append(dict(zip(header2,[item['review/userId'],item['product/productId'],item['review/score']])))
#for item in list2:
#	print list2
set_userid=set([])
set_productid=set([])
for item in list2:
	set_userid.add(item['userId'])
	set_productid.add(item['productId'])
for item in set_userid:
	rating_dict_user[item]={}
for item in list2:
	if item['productId']!='':
		rating_dict_user[item['userId']].update({item['productId'] : item['rating']})
ranges=[]
for product in set_productid:
	max1=max(product)
	min1=min(product)
	if(min1==''):
		min1=0.0
	if(max1==''):
		max1=0.0
	ranges.append((float(min1),float(max1)))
k=10
clusters=[]
for i in range(k):
	clusters.append([])
lastmatches=None
for j in range(k):
	item=0
	for item in ranges:
		val1=item[1]-item[0]
		val2=val1+item[0]
		val3=random.random()*val2
		clusters[j].append(val3)
list_userid=list(set_userid)
list_productid=list(set_productid)
for t in range(5):
	print t
	bestmatches=[[] for i in range(k)]
	for user in rating_dict_user:
		bestmatch=0
		for i in range(k):
			d=distance(clusters[i],rating_dict_user[user])
			if d<distance(clusters[bestmatch],rating_dict_user[user]): bestmatch=i
#			print d
		bestmatches[bestmatch].append(user)
		#print "skdjfh"+str(z)
#		z+=1
	if bestmatches==lastmatches:
		print "break"
		break
	lastmatches=bestmatches
	for i in range(k):
	 avgs=[0.0]*len(set_productid)
	 if len(bestmatches[i])>0:
	 	m=0
	 	for userid in bestmatches[i]:
	 		m=0
	 		for productid in rating_dict_user[userid]:
	 		 m=list_productid.index(productid)
	 		 if rating_dict_user[userid][productid]!='':
			 	avgs[m]+=float(rating_dict_user[userid][productid])
			# m+=1
	 	for j in range(len(avgs)):
	 		avgs[j]/=len(bestmatches[i])
	 	clusters[i]=avgs
writer=csv.writer(open("users_cluster.csv","wb"),quoting=csv.QUOTE_ALL)
for val in itertools.izip_longest(bestmatches[0],bestmatches[1],bestmatches[2],bestmatches[3],bestmatches[4],bestmatches[5],bestmatches[6],bestmatches[7],bestmatches[8],bestmatches[9],fillvalue=' '):
	writer.writerow(val)



