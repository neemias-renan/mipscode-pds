from django.contrib import admin

from .models import UserNew, UserSettings, Tutorial, Project, Documentation

class UsersettingsInline(admin.TabularInline):
    model = UserSettings
    extra = 0

    
class TutorialInline(admin.TabularInline):
    model = Tutorial
    extra = 0

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['name']}),
        (None,        {'fields': ['email']}),
        (None,        {'fields': ['password']}),        
        (None,        {'fields': ['bio']}),
        (None,        {'fields': ['avatar']}),
        (None,        {'fields': ['user_type']}),
    ]
    inlines = [TutorialInline,ProjectInline,UsersettingsInline]

class DocumentationArea(admin.TabularInline):
    model = Documentation


admin.site.register(UserNew,UserAdmin)
admin.site.register(Documentation)