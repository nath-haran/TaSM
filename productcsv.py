# from TaSM_site.models import Product
# import csv
# reader=csv.reader(open("Electronics.csv","r"))
# header=reader.next();
# line=reader.next();
# obj=Product.objects.create();
# obj.validate_unique();
# for line in reader:
# 	if len(line[1])>200:
# 		line[1]=line[1][:199]
# 	if line[2] == 'unknown':
# 		line[2]=0;
# 	obj.productid=line[0];
# 	obj.product_name=line[1];
# 	obj.price=line[2];
# 	obj.save();
# 	line=reader.next();


import csv
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
product_dict={}
list1=[]
list2=[]
set_productid=set([])
for row in reader:
	list1.append(dict(zip(header,row)))
header2=['productId','productTitle','price']
for item in list1:
	if item['review/userId']!='unknown':
		list2.append(dict(zip(header2,[item['product/productId'],item['product/title'],item['product/price']])))
set_productid=set([])
for item in list2:
	set_productid.add(item['productId'])
for item in set_productid:
	product_dict[item]={}
for item in list2:
	product_dict[item['productId']].update({item['productTitle'] : item['price']})
for item in product_dict:
	pid=item#product_dict[item]['productId']
	title=product_dict[item]['productTitle']
	price=product_dict[item]['price']
	if len(title)>200:
		title=title[:199]
	if price=='unknown':
		price=0.0
 	obj.productid=pid;
	obj.product_name=title;
	obj.price=price;
	obj.save();
	