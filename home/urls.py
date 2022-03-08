from django.urls import include, path
from home import views
from django.contrib.auth import views as auth_views


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
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='resetpassword/password_reset_done.html'), name='password_reset_done'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="resetpassword/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='resetpassword/password_reset_complete.html'), name='password_reset_complete'),
    path('email/', views.send_code, name="sendcode"),
    path('confirm_email/<uidb64>/<token>/', views.confirm_email, name='activate')
]
