from django.contrib import admin
from .models import Profile, LearningEntry

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')

@admin.register(LearningEntry)
class LearningEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
