from django.contrib import admin

from .models import User
from .models import Project, ProjectRequest

admin.site.register(User)
admin.site.register(Project)
admin.site.register(ProjectRequest)

