from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('contact/', views.contactPage.as_view(), name="contact"),
    # path('contact/', views.contactPage, name="contact"),
    path('signin/', views.signinPage, name="signin"),
    path('signup/', views.signupPage, name="signup"),
]
