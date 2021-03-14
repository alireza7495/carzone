from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" style="width:40px; border-radius:50%;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']
    sort = ['first_name']
    list_display = ['id', 'thumbnail', 'first_name', 'last_name', 'designation']
    list_display_links = ['first_name']


admin.site.register(Team, TeamAdmin)
