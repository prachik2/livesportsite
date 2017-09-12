from django.shortcuts import render , render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.core.urlresolvers import reverse

from flaskapp.forms import *
from flaskapp.models import *

# Create your views here.
def create_account(request,template_name = "create_account.html"):
	if request.method == "POST":
		create_account_form = CreateAccountForm(request.POST)
		if create_account_form.is_valid():
			cleaned_data = create_account_form.cleaned_data
			username = cleaned_data['user_name']
			email = cleaned_data['email']
			password = cleaned_data['password']
			
			user_object = User.objects.create_user(username = username,email = email, password = password)
			print  'Successfully user created '
			return HttpResponseRedirect(reverse('dashboard'))
	else:
		create_account_form = CreateAccountForm()
	return render(request, 'create_account.html', {'create_account_form': create_account_form})


def login_page(request):
	#import pdb; pdb.set_trace();
	if request.user.is_authenticated():
		print "user is  Authenticated"
		return HttpResponseRedirect(reverse('base'))

	if request.method == "POST":

		login_form = LogInForm(request.POST)
		if login_form.is_valid():
			cleaned_data = login_form.cleaned_data
			user_name= cleaned_data['username']
			pass_word= cleaned_data['password']
			
			user = authenticate(username=user_name, password=pass_word)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('dashboard'))
	else:
		login_form = LogInForm()
	return render(request, 'login.html', {'login_form': login_form})

def dashboard_page(request, template_name="dashboard.html"):
	
	if request.GET :
		sort_by = request.GET['sort_dropdown']
		order_list = {}
		if sort_by:
			if order_list:
				order_list = order_list.order_by(sort_by)
			else:
				order_list = Order.objects.order_by(sort_by)
	else:
		order_list = Order.objects.all()
	return render_to_response(template_name, {'order_list': order_list}, RequestContext(request))

def create_order_details(request,template_name ='create_order.html'):	

	if request.method == "POST":
		order_form = OrderDetailForm(request.POST)
		if order_form.is_valid():
			cleaned_data = order_form.cleaned_data
			order_id = cleaned_data['order_id']
			product_name = cleaned_data['product_name']
			order_status = cleaned_data['order_status']
			product_url = cleaned_data['product_url']
			cost_price = cleaned_data['cost_price']
			
			detail = Order.objects.create(order_id=order_id,product_name=product_name,order_status=order_status,product_url=product_url,cost_price=cost_price)
			detail.save()
			return HttpResponseRedirect(reverse('dashboard'))
	else :
		order_form = OrderDetailForm()
		print 'Details not updated!!'
	return render_to_response(template_name,{'order_form':order_form},RequestContext(request))	

def base(request,template_name = 'base.html'):
	message = 'You searched for: %s' % request
	print message
	return render(request, template_name)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect(reverse('base'))

