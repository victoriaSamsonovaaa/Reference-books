CREATE DATABASE HealthcareSystem;
USE HealthcareSystem;

-- Создание таблицы Отделения
CREATE TABLE Departments (
    department_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    location NVARCHAR(100) NOT NULL
);

-- Создание таблицы Врачи
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    specialty NVARCHAR(100) NOT NULL,
    department_id INT FOREIGN KEY REFERENCES Departments(department_id)
);

-- Создание таблицы Пациенты
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    address NVARCHAR(100) NOT NULL,
    doctor_id INT FOREIGN KEY REFERENCES Doctors(doctor_id),
    department_id INT FOREIGN KEY REFERENCES Departments(department_id),
    diagnosis NVARCHAR(100),
    diagnosis_description NVARCHAR(MAX),
    diagnosis_date DATE
);
