from django.contrib import admin

# Register your models here.
from myapp.models import TestTarget
admin.site.register(TestTarget)

from myapp.models import TestTodo
admin.site.register(TestTodo)

from myapp.models import User
admin.site.register(User)