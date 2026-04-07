from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
	raw_id_fields = ['likes']


class CommentAdmin(admin.ModelAdmin):
	list_display = ['post', 'author', 'published_at']
	raw_id_fields = ['post', 'author']


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
