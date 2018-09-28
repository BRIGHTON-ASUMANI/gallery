from django.conf.urls import url
from . import views

urlpatterns=[

    url('^$',views.picture_today,name='pictureToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pictures,name = 'pastImages'),
    url(r'^search/', views.search_results, name='search_results'),
]
