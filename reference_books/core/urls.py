from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Departments
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/<int:id_>/', views.department_detail, name='department_detail'),
    path('departments/<int:id_>/edit/', views.edit_department, name='edit_department'),
    path('departments/<int:id_>/delete/', views.delete_department, name='delete_department'),

    # Doctors
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/<int:id_>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/<int:id_>/edit/', views.edit_doctor, name='edit_doctor'),
    path('doctors/<int:id_>/delete/', views.delete_doctor, name='delete_doctor'),

    # Patients
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<int:id_>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:id_>/edit/', views.edit_patient, name='edit_patient'),
    path('patients/<int:id_>/delete/', views.delete_patient, name='delete_patient'),
]
