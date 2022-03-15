from django.urls import include, path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('myprofile/', views.my_profile, name="myprofile"),
    path('signup/', views.user_signup, name="signup"),
    path('<int:id>/', views.magazine, name="magazine"),
    path('<int:id>/<slug:slug>/', views.issue, name="issue"),
    path('contact/', views.contact, name="contact"),
    path('mymagazines/', views.mymags, name="mymagazines"),
    path('signout/', views.user_signout, name="signout"),
    path('saveissue/', views.save_issue, name="save-issue"),
    path('membership/', views.membership, name="membership"),
    path('staff/', views.staff, name="staff"),
    path('codes/', views.codes, name='codes'),
    path('email/', views.send_code, name="sendcode"),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('process-membership/',views.process_membership, name="process_membership"),
]
