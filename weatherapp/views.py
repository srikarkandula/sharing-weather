from django.shortcuts import render,HttpResponse,Http404,redirect

import urllib.request
import json
from django.contrib import messages


def index(request, *args , **kwargs):

    if request.method == 'POST':
        try:
            city = request.POST['city']

            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city + '&units=metric&appid=a3521e20e79ddfe8c4dcab7951006d57').read()

            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),
                "city": city,
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
            print(data)

        except:
            return render(request, 'notcity.html')


    else:
        data = {}

    return render(request, "index.html", data)



