from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified', 'timestamp')
    list_display_links = ('title',)
    list_filter = ('timestamp', 'modified')
    search_fields = ['title', 'text']
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)