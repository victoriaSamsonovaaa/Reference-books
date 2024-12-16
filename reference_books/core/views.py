from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Doctor, Patient


def index(request):
    return render(request, 'index.html')


# Departments
def department_list(request):
    sort_by = request.GET.get('sort', 'name')  # default sort by name, asc
    order = request.GET.get('order', 'asc')

    db_sort_by = f'-{sort_by}' if order == 'desc' else sort_by

    departments = Department.objects.all().order_by(db_sort_by)
    return render(request, 'department_list.html',
                  {'departments': departments, 'current_sort': sort_by, 'current_order': order})


def department_detail(request, id_):
    department = get_object_or_404(Department, id=id_)
    return render(request, 'department_detail.html', {'department': department})


def add_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        Department.objects.create(name=name, location=location)
        return redirect('department_list')
    return render(request, 'add_department.html')


def edit_department(request, id_):
    department = get_object_or_404(Department, id=id_)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.location = request.POST.get('location')
        department.save()
        return redirect('department_list')
    return render(request, 'edit_department.html', {'department': department})


def delete_department(request, id_):
    department = get_object_or_404(Department, id=id_)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'delete_department.html', {'department': department})


# Doctors
def doctor_list(request):
    sort_by = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')

    db_sort_by = f'-{sort_by}' if order == 'desc' else sort_by

    doctors = Doctor.objects.all().order_by(db_sort_by)
    return render(request, 'doctor_list.html', {'doctors': doctors, 'current_sort': sort_by, 'current_order': order})


def doctor_detail(request, id_):
    doctor = get_object_or_404(Doctor, id=id_)
    return render(request, 'doctor_detail.html', {'doctor': doctor})


def add_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialty = request.POST['specialty']
        department_id = request.POST['department_id']
        department = get_object_or_404(Department, id=department_id)
        Doctor.objects.create(name=name, specialty=specialty, department=department)
        return redirect('doctor_list')
    departments = Department.objects.all()
    return render(request, 'add_doctor.html', {'departments': departments})


def edit_doctor(request, id_):
    doctor = get_object_or_404(Doctor, id=id_)
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialty = request.POST.get('specialty')
        doctor.department_id = request.POST.get('department_id')
        doctor.save()
        return redirect('doctor_list')
    departments = Department.objects.all()
    return render(request, 'edit_doctor.html', {'doctor': doctor, 'departments': departments})


def delete_doctor(request, id_):
    doctor = get_object_or_404(Doctor, id=id_)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'delete_doctor.html', {'doctor': doctor})


# Patients
def patient_list(request):
    sort_by = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')

    db_sort_by = f'-{sort_by}' if order == 'desc' else sort_by

    patients = Patient.objects.all().order_by(db_sort_by)
    return render(request, 'patient_list.html', {'patients': patients, 'current_sort': sort_by, 'current_order': order})


def patient_detail(request, id_):
    patient = get_object_or_404(Patient, id=id_)
    return render(request, 'patient_detail.html', {'patient': patient})


def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        birth_date = request.POST['birth_date']
        address = request.POST['address']
        doctor_id = request.POST['doctor_id']
        department_id = request.POST['department_id']
        diagnosis = request.POST.get('diagnosis', '')
        diagnosis_description = request.POST.get('diagnosis_description', '')
        diagnosis_date = request.POST.get('diagnosis_date', None)
        if diagnosis_date == '':
            diagnosis_date = None
        doctor = get_object_or_404(Doctor, id=doctor_id)
        department = get_object_or_404(Department, id=department_id)
        Patient.objects.create(
            name=name, birth_date=birth_date, address=address,
            doctor=doctor, department=department, diagnosis=diagnosis,
            diagnosis_description=diagnosis_description, diagnosis_date=diagnosis_date
        )
        return redirect('patient_list')
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    return render(request, 'add_patient.html', {'doctors': doctors, 'departments': departments})


def edit_patient(request, id_):
    patient = get_object_or_404(Patient, id=id_)
    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.birth_date = request.POST.get('birth_date')
        patient.address = request.POST.get('address')
        patient.doctor_id = request.POST.get('doctor_id')
        patient.department_id = request.POST.get('department_id')
        patient.diagnosis = request.POST.get('diagnosis')
        patient.diagnosis_description = request.POST.get('diagnosis_description')
        diagnosis_date = request.POST.get('diagnosis_date')
        if diagnosis_date == '':
            diagnosis_date = None
        patient.diagnosis_date = diagnosis_date
        patient.save()
        return redirect('patient_list')
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    patient.birth_date = str(patient.birth_date)  # чтобы при подстановке в html показывалась дата в формате yyyy-mm-dd
    patient.diagnosis_date = str(patient.diagnosis_date)
    return render(request, 'edit_patient.html', {'patient': patient, 'doctors': doctors, 'departments': departments})


def delete_patient(request, id_):
    patient = get_object_or_404(Patient, id=id_)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'delete_patient.html', {'patient': patient})
