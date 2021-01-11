from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.employee_form, name='employee_insert'),               # get and post insert operation
    path('list/',views.employee_list,name='employee_list'),             # get and post request update operation
    path('<int:id>/',views.employee_form, name='employee_update'),      # get request to retrive and display all records
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
]