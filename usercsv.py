# from product.models import User
# import csv
# reader=csv.reader(open("arts.csv","r"));
# header=reader.next();
# line=reader.next();
# obj=User.objects.create();
# obj.validate_unique();
# for line in reader:
# 	User.objects.create(userid=line[3],username=line[4])
# 	#obj.userid=line[3];
# 	#obj.username=line[4];
# 	#obj.save();
# 	line=reader.next();
# from product.models import User


from TaSM_site.models import User
import csv
reader=csv.reader(open("arts.csv","r"))
header=reader.next()
user_dict={}
list1=[]
list2=[]
set_userid=set([])
for row in reader:
	list1.append(dict(zip(header,row)))
header2=['userId','username']
for item in list1:
	if item['review/userId']!='unknown':
		list2.append(dict(zip(header2,[item['review/userId'],item['review/profileName']])))
set_userid=set([])
for item in list2:
	set_userid.add(item['userId'])
for item in set_userid:
	user_dict[item]={}
for item in list2:
	user_dict[item['userId']].update({'name':item['username']})

obj=User()
obj.validate_unique();


for item in user_dict:
	uid=item#product_dict[item]['productId']
	name=user_dict[item]['name']
	#price=product_dict[item]['price']
	if len(name)>200:
		name=name[:199]
	# if price=='unknown':
	# 	price=0.0
 	obj.userid=uid;
	obj.username=name;
	obj.email=uid+"@gmail.com"
	obj.save();
