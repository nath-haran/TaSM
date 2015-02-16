
# import csv
# reader=csv.reader(open("arts.csv","r"))
# header=reader.next();
# line=reader.next();

# obj.validate_unique();



# for line in reader:
# 	obj=Transaction()
# 	#obj=Transaction.objects.create(productid=line[0],userid=line[3],rating=line[6],rating_time=line[7],review=line[8])
# 	#obj.userid=str(line[3]);
# 	#obj.productid=str(line[0]);
# 	obj.rating=line[6];
# 	obj.rating_time=line[7];
# 	obj.review=line[8];
# 	obj.save();
# 	line=reader.next();
from TaSM_site.models import Transaction
import csv
import datetime
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
product_dict={}
list1=[]
list2=[]
for row in reader:
	list1.append(dict(zip(header,row)))
#list_id=[]
header2=['userId','productId','rating','time']
list2=[]
for item in list1:
	if item['review/userId']!='unknown' and item['review/userId']!='':
		if item['review/time']=='unknown' or item['review/time']=='':
			date_time=datetime.datetime.now()
		else:
			date_time=datetime.datetime.fromtimestamp(float(item['review/time']))
		list2.append(dict(zip(header2,[item['review/userId'],item['product/productId'],item['review/score'],date_time])))
# set_userid=set([])
# set_productid=set([])
# for item in list2:
# 	set_userid.add(item['userId'])
# 	set_productid.add(item['productId'])

# for item in set_productid:
# 	rating_dict_product[item]={}
# for item in list2:
# 	rating_dict_product[item['productId']].update({item['userId'] : [[item['rating']})
for item in list2:
	obj=None
	obj=Transaction.objects.filter(productid=item['productId'],userid=item['userId'])
	if len(obj)==0:
		obj=Transaction();
		#obj.validate_unique();
		obj.userid=item['userId']
		obj.productid=item['productId']
		obj.rating=int(float(item['rating']))
		print obj.rating
		obj.rating_time=item['time']
		obj.save()
# for item1 in rating_dict_product:
# 	for item2 in rating_dict_product[item]:
# 		obj.rating=rating_dict_product[item1][item2];
# 	 	obj.rating_time=line[7];

# 	obj.save();