from django.urls import path
from attendance_app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('log_in',views.log_in,name='log_in')
]
