from django.conf.urls import url
from api import views

urlpatterns=[
url(r'^stat/$',views.CHapi, name='CHapi'),]
