from django.contrib import admin
from .models import Form, User, Report

class UserModelAdmin(admin.ModelAdmin):
    exclude = ('password',) 

admin.site.register(Form)
admin.site.register(User, UserModelAdmin)
admin.site.register(Report)
