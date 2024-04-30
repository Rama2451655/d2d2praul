from django.urls import path
from d2d2app.views import template
urlpatterns=[
    path('',template,name='template')
]