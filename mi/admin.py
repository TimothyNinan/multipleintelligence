from django.contrib import admin
from .models import User, Class, Questions, Results

# Register your models here.
admin.site.register(User)
admin.site.register(Class)
admin.site.register(Questions)
admin.site.register(Results)