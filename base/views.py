from django.shortcuts import render,redirect
from django.urls import reverse
import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import *
from django.utils.html import strip_tags

# Create your views here.
stripe.api_key = 'sk_test_51ImyQ8SC7arSahr84qFozEBYpj16zY0rmrRfR5hOqnNStE1pzNJ8AsaRBXOGftMjCNviCxq75EKtvcGtxLeHewNb00H2CiWiWB'

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')


def charge(request):


	if request.method == 'POST':
		amount = int(request.POST['amount'])
		email=request.POST['email']
		name=request.POST['name']
		mobile_no=request.POST['mobile']

		#session created
		request.session['amnt'] = amount
		request.session['name'] = name
		request.session['email'] = email
		request.session['mobile_no'] = mobile_no
		
		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Donation"
			)
	context = {
		'amount' : request.session.get('amnt'),
		'name' : request.session.get('name'),
		'mobile_no': request.session.get('mobile_no'),
		}
	html_content = render_to_string("email.html",context)
	text_content = strip_tags(html_content)
	email = EmailMultiAlternatives(
		"Donation",
		text_content,
		settings.EMAIL_HOST_USER,
		[email]
	)
	email.attach_alternative(html_content, "text/html")
	email.send()
	return render(request,'success.html')

def success(request):
	return render(request, 'success.html')

def invoice(request):
	
	context = {
		'amount' : request.session.get('amnt'),
		'name' : request.session.get('name'),
		'email' : request.session.get('email'),
		'mobile_no': request.session.get('mobile_no'),
		}
	return render(request, 'invoice.html',context)

def email(request):
	context = {
		'amount' : request.session.get('amnt'),
		'name' : request.session.get('name'),
		'email' : request.session.get('email'),
		'mobile_no': request.session.get('mobile_no'),
		}
	return render(request, 'email.html',context)