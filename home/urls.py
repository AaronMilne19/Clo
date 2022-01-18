from django.urls import include, path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('myprofile/', views.my_profile, name="myprofile"),
    path('signup/', views.user_signup, name="signup"),
    path('<int:id>', views.magazine, name="magazine"),
    path('<int:id>/<slug:slug>/', views.issue, name="issue"),
    path('contact/', views.contact, name="contact"),
    path('signout/', views.user_signout, name="signout"),
    path('membership/', views.membership, name="membership"),
    path('contact/',views.contact, name="contact"),

]
