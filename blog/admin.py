from django.contrib import admin

# Register your models here.
#Superuser
#Name: amon
#PW: otsukiamon35220925

from django.contrib import admin
from .models import Post#Check what . means
from django.contrib import admin
from .models import Post

admin.site.register(Post)
