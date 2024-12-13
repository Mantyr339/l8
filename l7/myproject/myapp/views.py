from django.shortcuts import render
from l7.myproject.myapp.models import Department, Position, Employee, Project

def index(request):
    departments = Department.objects.all()
    positions = Position.objects.all()
    employees = Employee.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {
        'departments': departments,
        'positions': positions,
        'employees': employees,
        'projects': projects,
    })
