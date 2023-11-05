from django.contrib import admin
from .models import Form, User, Report, RateDate

class UserModelAdmin(admin.ModelAdmin):
    exclude = ('password',) 

admin.site.register(Form)
admin.site.register(User, UserModelAdmin)
admin.site.register(Report)
admin.site.register(RateDate)
