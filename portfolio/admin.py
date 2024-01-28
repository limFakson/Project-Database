from django.contrib import admin
from .models import Project, AboutData

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link')
    
class AboutDataAdmin(admin.ModelAdmin):
    list_display = ('syntax', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(AboutData, AboutDataAdmin)