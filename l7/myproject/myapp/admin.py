from django.contrib import admin
from .models import Department, Position, Employee, Project, ProjectExecution


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(ProjectExecution)
