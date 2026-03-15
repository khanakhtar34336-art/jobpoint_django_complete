from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Job
from .models import Profile



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('is_employer',)}),
    )

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'posted_at')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'contact',
        'degree',
        'institute',
        'graduation_year',
        'Edit',
    )
     
    fields = (
        'user',
        'contact',
        'about',
        'degree',
        'institute',
        'graduation_year',
        'profile_photo',
        'resume',
        'is_employer',

    )
    list_display = (
    'user',
    'contact',
    'degree',
    'institute',
    'graduation_year',
    'is_employer',   # ✅
)
