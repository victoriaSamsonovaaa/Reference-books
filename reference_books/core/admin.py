from django.contrib import admin
from .models import Department, Doctor, Patient


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', )


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'department')
    search_fields = ('name', 'department__name')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'address', 'doctor', 'department',
                    'diagnosis', 'diagnosis_description', 'diagnosis_date')
    search_fields = ('name', 'doctor__name', 'department__name')
