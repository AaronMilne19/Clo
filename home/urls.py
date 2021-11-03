from django.urls import include, path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
]