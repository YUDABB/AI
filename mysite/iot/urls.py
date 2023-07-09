from django.urls import path
from . import views
app_name='iot'

urlpatterns = [
    path('',views.index,name='index'),

]