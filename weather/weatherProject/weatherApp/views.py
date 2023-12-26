from django.shortcuts import render
from . models import climate
import requests
from . forms import climateform

# Create your views here
def weather(request):
    url = ("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID={}")
    if request.method == "POST":
        form=climateform(request.POST)
        form.save()
    form=climateform
    weather_data=[]
    for villages in climate.objects.all():
        print(villages)
        r = requests.get(url.format(villages,'fabdaa97312a385e4a1358103bdee99b')).json()
        print(r) 
        weather = {
            'city' : villages,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        
        weather_data.append(weather)
        
        context = {'weather_data' : weather_data,'form':form}
    return render(request, 'index.html', context)