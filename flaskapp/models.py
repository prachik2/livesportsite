from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Order(models.Model):
	order_id = models.CharField(max_length=30,null=True)
	product_name = models.CharField(max_length =140)
	order_status = models.CharField(max_length = 20)
	order_date = models.DateTimeField(auto_now_add=True, null=True)
	order_deadline = models.DateTimeField(auto_now_add=True, null=True)
	order_source = models.CharField(max_length=30)
	product_code = models.CharField(max_length = 30)
	product_url = models.URLField()
	cost_price = models.CharField(max_length = 10)
	customer_name = models.CharField(max_length = 20)
	selling_price = models.CharField(max_length = 10)
	quantity = models.CharField(max_length = 10)
	customer_email = models.CharField(max_length = 50)
	customer_phone = models.CharField(max_length = 12)
	customer_address = models.CharField(max_length =100)
	payment_type = models.CharField(max_length = 10)
	procurement_status = models.CharField(max_length = 40)
	procurement_date = models.DateTimeField(auto_now_add=True, null=True)
	supplier = models.CharField(max_length =50)
	package_id = models.CharField(max_length = 30)
	consolidation_id = models.CharField(max_length=30 ,null=True)
	usa_tracking = models.CharField(max_length = 255)
	tracking_number = models.CharField(max_length =30)
	cost_price = models.CharField(max_length =10)	
	comments = models.CharField(max_length = 50)
	edit_log = models.CharField(max_length =20)
	# def order_id_required(self):
	# 	if order_id in Order.objects.values_list('name',flat = True):
	# 		return order_id.clean('')
