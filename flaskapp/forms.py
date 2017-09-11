from django import forms
from django import views
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import (
	check_password, is_password_usable, make_password,
)

class CreateAccountForm(forms.Form):
	
	user_name = forms.CharField(label = "Username",widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
	email = forms.EmailField(label = "Email",widget=forms.TextInput(attrs={'placeholder': 'Email Id'}))
	password = forms.CharField(min_length = 7,label = 'Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	def clean_email(self):
		cleaned_data = self.cleaned_data
		email = cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Email already exists. Enter another Valid Email")
		return email


class LogInForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		cleaned_data = self.cleaned_data
		username = cleaned_data.get('username')
		if not User.objects.filter(username=username):
			raise forms.ValidationError('User is not Registered.\n Try again')
		return username

	def clean_password(self):
		cleaned_data = self.cleaned_data
		username = cleaned_data.get('user_name')
		password = cleaned_data.get('pass_word')
		user = User.objects.filter(username = username) 
		if user.exists() and not user[0].check_password(password):
			print "you entered wrong password."
			raise forms.ValidationError('Wrong Password.Retype your password.')
		return password

class OrderDetailForm(forms.Form):
	order_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Order id'}))
	product_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product Name'}))
	order_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Order status'}))
	product_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product URL'}))
	cost_price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Cost Price'}))

	# def clean_order_id(self):
	# 	cleaned_data = self.cleaned_data
	# 	order_id = cleaned_data.get('order_id')
	# 	product_name = cleaned_data.get('product_name')
	# 	if order_id and product_name:
	# 		if Order.objects.filter(order_id=order_id).exists():
	# 			raise forms.ValidationError("Order id already exists")
	# 		return order_id
