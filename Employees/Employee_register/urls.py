from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('list/', views.employee_list, name='employee_list'),

]