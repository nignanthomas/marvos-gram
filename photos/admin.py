from django.contrib import admin
from .models import Image,Comments,Follow,Profile

# Register your models here.
admin.site.register(Image)
admin.site.register(Follow)
admin.site.register(Comments)
admin.site.register(Profile)
