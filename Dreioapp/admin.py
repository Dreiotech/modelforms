from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Employee
from .models import Post

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Employee)
admin.site.register(Post)