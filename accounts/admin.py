from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "created_at", "updated_at"]
    search_fields = ["name", "email"]
    list_filter = ["created_at", "updated_at"]
    
    
    class Meta:
        model = User
        
admin.site.register(User, UserAdmin)