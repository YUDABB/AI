from django.urls import path
from . import views
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('q_register/', views.q_register, name='q_register'),
    path('<int:q_id>/', views.detail, name='detail'),
    path('up/<int:q_id>/', views.up, name='up'),
    path('delete/<int:q_id>/', views.delete, name='delete'),
    path('answer/register/<int:q_id>', views.a_register, name='a_register'),
]
