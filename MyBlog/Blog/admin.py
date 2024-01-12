from django.contrib import admin
from Blog.models import BlogPost,AuthorizationRequest
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(AuthorizationRequest)