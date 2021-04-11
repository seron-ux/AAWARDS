from django.contrib import admin
from .models import Post
admin.site.site_header='seron'


admin.site.register(Post)
