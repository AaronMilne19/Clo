from django.urls import include, path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('signup/', views.user_signup, name="signup"),
    path('<int:id>', views.magazine, name="magazine"),
    path('<int:id>/<slug:slug>/', views.issue, name="issue"),
    path('signout/', views.user_signout, name="signout"),
    path('contact/',views.contact, name="contact"),
]
