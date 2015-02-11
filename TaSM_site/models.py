from django.db import models
import datetime
class User(models.Model):
	userid=models.CharField(primary_key=True,max_length=200)
	username=models.CharField(default='user',max_length=200)
	password=models.CharField(default='password',max_length=200)
	def __str__(self):
		return self.username

class Product(models.Model):
	productid=models.CharField(primary_key=True,max_length=200)
	product_name=models.CharField(max_length=200)
	product_price=models.CharField(default=0.0,max_length=200)
	def __str__(self):
		return self.product_name


class Transaction(models.Model):
	userid=models.CharField(max_length=200,db_column='userid')#ForeignKey(User)
	productid=models.CharField(max_length=200,db_column='productid') # ForeignKey(Product)
	rating=models.IntegerField(default=0.0)
	rating_time=models.DateTimeField()
	class Meta:
		unique_together=('userid','productid')
	
# Create your models here.
