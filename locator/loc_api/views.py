import requests
import pprint,json
from django.shortcuts import render 
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect, JsonResponse
from .models import locate_model_yelp
from rest_framework.views import APIView 
from serializers import locate_model_yelpSerializer
from rest_framework.response import Response




def locate_yelp(request, city):       #  *** YELP API CALL ***
    app_id = 'oqjRCS9bgq2hkM9TQNHqDQ'
    app_secret='jitwH4kSfI3BrPj4mLaf44kgdJllKCUdoJuPNosTTeiawS9DRDpDSp8cHeOIJiGR'

    data = {'grant_type': 'client_credentials',
            'client_id': app_id,
            'client_secret': app_secret}

    token = requests.post('https://api.yelp.com/oauth2/token', data=data)

    access_token = token.json()['access_token']
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' % access_token}
    params = {
    	'location': city                                       # city is used as a parameter in the GET request                  
        }

    resp = requests.get(url=url, params=params, headers=headers)
    #print resp.url
    resp = resp.json()
    data = {
    	'name' : resp.get('businesses')[0].get('location'),
    	#'coords' : resp.get('businesses')[0].get('coordinates')  * other attributes as per choice *
    }

    return JsonResponse(data)   # *** returns JSON response ***





def locate_foursquare(request,city):        #  *** FOURSQUARE API CALL ***
    url = 'https://api.foursquare.com/v2/venues/search?near=%s' %city

    params = dict(
                    client_id='BZHQ3HD4SWX0ATW3NS4LLKMVAUG4F4DKREDA1O1EKZ3R42EF',
                    client_secret='CKLZPJHBNUMFJ440BEIQMDLHRXOTBVIANN5JATGDVNSQIS1J',
                    v='20170801',
                    query='coffee',
                    near = city ,
                    limit=10
    )
    resp = requests.get(url=url, params=params)
    resp = resp.json()
    data = {
            'city': resp.get('response').get('venues')[0].get('location').get('city'),
            'country':resp.get('response').get('venues')[0].get('location').get('country'),
            'venue':resp.get('response').get('venues')[0].get('name'),
            'postal_code':resp.get('response').get('venues')[0].get('location').get('postalCode'),
            'address':resp.get('response').get('venues')[0].get('location').get('address'),
            'state':resp.get('response').get('venues')[0].get('location').get('state'),
            'display_address':resp.get('response').get('venues')[0].get('location').get('formattedAddress')[0],
    
            }



    return JsonResponse(data)



def save_result_yelp(request,city):
    app_id = 'oqjRCS9bgq2hkM9TQNHqDQ'
    app_secret = 'jitwH4kSfI3BrPj4mLaf44kgdJllKCUdoJuPNosTTeiawS9DRDpDSp8cHeOIJiGR'

    data = {'grant_type': 'client_credentials',
            'client_id': app_id,
            'client_secret': app_secret}

    token = requests.post('https://api.yelp.com/oauth2/token', data=data)

    access_token = token.json()['access_token']
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' % access_token}
    params = {
        'location': city                       
        }

    resp = requests.get(url=url, params=params, headers=headers)
    resp = resp.json()

    data = {
        'name' : resp.get('businesses')[0].get('location'),
    }
    
                
    saving_data =  locate_model_yelp.objects.create(country = data['name']['country'],
                                                    city = data['name']['city'],
                                                    display_address = data['name']['display_address'][1],
                                                    state = data['name']['state'],
                                                    address1 = data['name']['address1'],
                                                    zip_code = data['name']['zip_code'],
                                                    api_used = "yelp"
                                                    )

    return HttpResponse(" Data Saved !") 




def save_result_foursquare(request,city):
    url = 'https://api.foursquare.com/v2/venues/search?near=%s' %city

    params = dict(
                    client_id='BZHQ3HD4SWX0ATW3NS4LLKMVAUG4F4DKREDA1O1EKZ3R42EF',
                    client_secret='CKLZPJHBNUMFJ440BEIQMDLHRXOTBVIANN5JATGDVNSQIS1J',
                    v='20170801',
                    query='coffee',
                    near = city ,
                    limit=10
    )
    resp = requests.get(url=url, params=params)
    
    resp = resp.json()
    data = {
            'city': resp.get('response').get('venues')[0].get('location').get('city'),
            'country':resp.get('response').get('venues')[0].get('location').get('country'),
            'venue':resp.get('response').get('venues')[0].get('name'),
            'postal_code':resp.get('response').get('venues')[0].get('location').get('postalCode'),
            'address':resp.get('response').get('venues')[0].get('location').get('address'),
            'state':resp.get('response').get('venues')[0].get('location').get('state'),
            'display_address':resp.get('response').get('venues')[0].get('location').get('formattedAddress')[0],
    
            }
    saving_data =  locate_model_yelp.objects.create(
                                                    country = data['country'],
                                                    city = data['city'],
                                                    display_address = data['display_address'],
                                                    state = data['state'],
                                                    address1 = data['address'],
                                                    zip_code = data['postal_code'],
                                                    venue = data['venue'],
                                                    api_used = "foursqaure",
     )                                                  
                                                    
                                                    
    
    return HttpResponse(" Data Saved !")





class Locate_API(APIView):    # API view of the saved results in the database

    def get(self,request):
        results = locate_model_yelp.objects.all()
        serializer = locate_model_yelpSerializer(results, many = True)

        return Response(serializer.data)
        






