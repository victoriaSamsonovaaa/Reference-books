from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctors")

    def __str__(self):
        return f"{self.name} - {self.specialty}"


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="patients")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="patients")
    diagnosis = models.CharField(max_length=100, blank=True, null=True)
    diagnosis_description = models.TextField(blank=True, null=True)
    diagnosis_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
