from django.shortcuts import render, get_object_or_404
import requests
import json
from geopy.geocoders import Nominatim
from datetime import date, timedelta
from .models import Post,Category

# Create your views here.

def index(request):
	app_name = Nominatim(user_agent="RapidLens")
	locator = app_name.geocode("bosso")

	todays_date = date.today()

	API_key = 'fe630c653cc821cac7e40242262840a0'
	lat = str(locator.latitude)
	lon = str(locator.longitude)
	location = locator.address
	source = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' +lat+ '&lon='+lon+ '&exclude=hourly,minutely&units=metric&appid='+API_key)
	status = source.status_code
	result = source.json()
	print(status, lat, lon)
	print(location)
	#print(result)

	# for today in result['current']:
	# 	day = dict( current = todays_date, temperature=today.temperature)
	# 	print(day)
	# 	print( '{current} **** {temperature}'.format(**day))
	# 	todays_date += timedelta(days=1)

	data = {
		"location": str(locator),
		"temparature":str(round(result['current']['temp'])),
		"current_weather":str(result['current'])

	}
	print(data)
	return render(request, 'index.html',data)

def news(request):
	posts = Post.published.all()
	headlines = Post.published.all()
	category = Category.objects.all()
	return render(request, 'news.html', {'posts':posts, 'category':category, 'headlines':headlines})

def detail(request,year,month,day,details):
	category = Category.objects.all()
	headlines = Post.published.all()
	details = get_object_or_404(Post,slug=details, status='published', publish__year=year,publish__month=month,publish__day=day)
	return render(request, 'details.html',{'details':details, 'headlines':headlines, 'category':category})
	
def contact(request):
	return render(request, 'contact.html')
	
