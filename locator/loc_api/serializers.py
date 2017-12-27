from rest_framework import serializers
from .models import locate_model_yelp

class locate_model_yelpSerializer(serializers.ModelSerializer):

    class Meta:

    	model = locate_model_yelp
    	fields = '__all__'
    	

