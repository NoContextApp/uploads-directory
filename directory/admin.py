from django.contrib import admin
from .models import Platform, Tag, File

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
    

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'platform', 'reply_count', 'like_count', 'repost_count', 'source', 'file', 'created_at', 'updated_at')
    list_select_related = ('platform',)
    # search
    search_fields = ('platform__name', 'tags__name', 'source')
    
    autocomplete_fields = ('tags',)


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(File, FileAdmin)