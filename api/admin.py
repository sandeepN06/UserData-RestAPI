from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','age','email','mobile_no','education','city','create_at']
    
