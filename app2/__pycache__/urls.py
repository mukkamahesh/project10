from django.urls import path
from app2.views import *
app_name='anything'
urlpatterns=[
    path('a2_first/',a2_first,name='a2_first'),
]