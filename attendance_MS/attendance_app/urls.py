from django.urls import path
from attendance_app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login')
]
