from django.urls import path

from book import views

from .views import *

app_name = 'book'
urlpatterns = [

    path('emp-gcreate/', views.EmployeeCreate.as_view(), name='EmployeeCreate'),
    path('emp-retr/', views.EmployeeRetrieve.as_view(), name='EmployeeRetrieve'),
    path('emp-retr/<int:pk>/', views.EmployeeDetail.as_view(), name='EmployeeDetail'),
    path('emp/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='EmployeeUpdate'),
    path('emp/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='EmployeeDelete'),

]

