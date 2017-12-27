from django.conf.urls import url
from django.contrib import admin
from loc_api.views import locate_yelp,locate_foursquare, Locate_API , save_result_yelp,save_result_foursquare
from rest_framework.urlpatterns import format_suffix_patterns
 



urlpatterns = [ 
				   url(r'^admin/', admin.site.urls),
				   url(r'^instalocate-yelp/(?P<city>[\w-]+)/$',locate_yelp),
   				   url(r'^instalocate-foursquare/(?P<city>[\w-]+)/$',locate_foursquare),
   		     	   url(r'^api.instalocate/$',Locate_API.as_view()),
   		     	   url(r'^instalocate-foursquare/(?P<city>[\w-]+)/save$',save_result_foursquare),
   		     	   url(r'^instalocate-yelp/(?P<city>[\w-]+)/save$',save_result_yelp),

			  ]

urlpatterns = format_suffix_patterns(urlpatterns)