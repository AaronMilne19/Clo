from django.urls import include, path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('<slug:slug>/', views.magazine, name="magazine"),
]