from django.conf.urls import url
from .models import *
from . import views

urlpatterns = [
	#--------------------------------------Sign in Page/Sign Up page-----------------------------#
	url(r'^create_account/',views.create_account,name = 'create_account'),
	url(r'^dashboard/',views.dashboard_page,name = 'dashboard'),
	url(r'^login/',views.login_page,name = 'login'),
	url(r'^create_order/',views.create_order_details,name = 'create_order'),
	url(r'^base/',views.base,name = 'base'),
	url(r'^logout_page/',views.logout_page,name='logout_page'),

	]