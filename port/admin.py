from django.contrib import admin
from.models import Profile2

class portAdmin(admin.ModelAdmin):
    list_display=('name','email','dob','address','linkedin')

admin.site.register(Profile2)
