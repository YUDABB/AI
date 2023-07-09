from django.urls import path
from . import views
app_name='p_ck'

urlpatterns = [
    path('<int:u_id>/',views.index,name='index'),
    path('detail/<int:q_id>/', views.detail, name='detail'),
    path('up/<int:q_id>/', views.up, name='up'),
]
