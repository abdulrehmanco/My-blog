from django.contrib import admin
from home.models import Rabtaguzari, blogpost,blogcomment
# Register your models here.
admin.site.register(Rabtaguzari),
admin.site.register(blogpost),
admin.site.register(blogcomment)