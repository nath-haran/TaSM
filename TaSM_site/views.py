from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader,Context
from TaSM_site.models import User
from TaSM_site.models import Transaction
# Create your views here.
from django.shortcuts import render_to_response
from math import sqrt
import csv
from django.db import connection
import numpy as np


#pearson


rating_dict={}
set_userid=set([])
set_productid=set([])


def calculate_similarity(item1,item2,rating_dict_product,avg_rating):
	num=0
	num1=0
	num2=0
	den1=0
	den2=0
	for key1 in rating_dict_product[item1]:
		#print "inside for"
		if rating_dict_product[item2].has_key(key1):
			avg=avg_rating[key1]
		#	print "inside if"
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
	#print den
	#if num==0:
	#	return 0
	if den==0:
		return 0
	return num/(den)




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


#pearson
def home(request):
	user=request.user
	template1=loader.get_template('home.html')
	id=user.email
	cur_user=User.objects.filter(email=id).values()[0]['userid']
	#c=Context({"id":cur_user['email'],"username":cur_user['userid']})
	#transactions=Transaction.objects.all().values()
	# transaction_list=transactions.values();
	# for item in transactions:
	# 	print item
	reader=csv.reader(open('users_cluster.csv','rb'))
	clusters=[]
	for i in range(10):
		clusters.append([])
	for row in reader:
		for i in range(len(row)):
			if row[i]!='' and row[i]!=' ':
				clusters[i].append(row[i])
	user_cluster=-1
	m=0
	for  cluster in clusters:
		for i in range(len(cluster)):
			if cluster[i]==cur_user:
				user_cluster=m
		if user_cluster!=-1:
			break;
		m+=1
	transactions=Transaction.objects.filter(userid__in=clusters[user_cluster]).values()
	cursor=connection.cursor()
	cursor.execute("select productid,count(*) from TaSM_site_transaction group by productid order by count(*) desc")
	product_count=dict(cursor.fetchall())

	for item in transactions:
		set_userid.add(item['userid'])
		set_productid.add(item['productid'])
	for item in set_userid:
		rating_dict[item]={}
	distance_list=[]
	for item in transactions:
	 	rating_dict[item['userid']].update({item['productid'] : item['rating']})
	user_dict=rating_dict[cur_user]
	distance_list=[]
	for user in set_userid:
		if user!=cur_user:
			distance=0
			distance=pearson(cur_user,user)
			distance_list.append({'name': user,'distance':distance})
	sorted_distance_list=sorted(distance_list,key= lambda k : k['distance'],reverse=True)
	recommendations=set([])
	i=0
	for item in distance_list:
		#if len(recommendations)<10:
		if i<100:
			for product in rating_dict[item['name']]:
				if not product in user_dict:
					recommendations.add((product,product_count[product]))
		else:
			break
		i+=1
	recommendations=sorted(recommendations,key=lambda x : x[1],reverse=True)[:10]
	return render_to_response('home.html', {'recommendations':recommendations}, context_instance=RequestContext(request))
	# return HttpResponse(template1.render(c))

def product(request,id):
	# user=request.user
	# id=user.email
	# template1=loader.get_template('product.html')
	# cur_user=User.objects.filter(email=id).values()[0]['userid']
	reader=csv.reader(open('products_cluster.csv','rb'))

	clusters=[]
	for i in range(5):
		clusters.append([])
	for row in reader:
		for i in range(len(row)):
			if row[i]!='' and row[i]!=' ':
				clusters[i].append(row[i])
	product_cluster=-1
	m=0
	for  cluster in clusters:
		for i in range(len(cluster)):
			if cluster[i]==id:
				product_cluster=m
		if product_cluster!=-1:
			break;
		m+=1
	#product_cluster-=1
	transactions=Transaction.objects.filter(productid__in=clusters[product_cluster]).values()	
	cursor=connection.cursor()
	cursor.execute("select productid,count(*) from TaSM_site_transaction group by productid order by count(*) desc")
	product_count=dict(cursor.fetchall())
	set_userid=set([])
	set_productid=set([])
	rating_dict_product={}
	rating_dict_users={}
	set_productid=set(clusters[product_cluster])
	# for item in transactions:
	# #	set_userid.add(item['userId'])
	# 	set_productid.add(item['productid'])
	for item in set_productid:
		rating_dict_product[item]={}
	for item in transactions:
		rating_dict_product[item['productid']].update({item['userid'] : item['rating']})
	transactions=Transaction.objects.all().values()
	for item in transactions:
		set_userid.add(item['userid'])
	#	set_productid.add(item['productId'])
	
	for item in set_userid:
		rating_dict_users[item]={}

	for item in transactions:
		rating_dict_users[item['userid']].update({item['productid'] : item['rating']})
	avg_rating={}
	# for key in set_userid:
	# 	avg_rating[key]={}
	for user in rating_dict_users:
		summ=0
		count=0
		for key in rating_dict_users[user]:
			if rating_dict_users[user][key]!='' and rating_dict_users[user][key]!='unknown':
				summ+=float(rating_dict_users[user][key])
				count+=1
		if count!=0:
			avg_rating.update({user:float(float(summ)/count)})
			# avg_rating[user]=float(float(summ)/count)
		else:
			avg_rating.update({user:float(0)})
			#avg_rating[user]=0

	i=0
	j=0
	length=len(set_productid)

	distance_matrix=np.ndarray(shape=(length),dtype=float,order='F')
	for item1 in set_productid:
		similarity=0
		#if item1!=id:
			#similarity=float(0)
		similarity=calculate_similarity(item1,id,rating_dict_product,avg_rating)
		distance_matrix[j]=similarity
		j+=1


	j=0
	related_dict=[]
	for item1 in set_productid:
		
		if item1!=id:
			related_dict.append((item1,distance_matrix[j]))
			print j
		j+=1

	
	recommendations=set([])
	for item in related_dict:
		if len(recommendations)<100:
			recommendations.add((item[0],product_count[item[0]]))

	recommendations=sorted(recommendations,key=lambda x : x[1],reverse=True)[:10]
	return render_to_response('product.html', {'recommendations':recommendations}, context_instance=RequestContext(request))


	# count=0
	# for item1 in cluster1:
	# 	for item2 in cluster1:
	# 		similarity=0
	# 		if item1!=item2:
	# 			#similarity=float(0)
	# 			similarity=calculate_similarity(item1,item2,rating_dict_product,avg_rating)
	# 			if similarity!=float(0):
	# 				count+=1
	# 		j+=1
	