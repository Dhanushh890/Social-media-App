from django.urls import path
from sma_app import views


urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.signin,name='signin')
]
