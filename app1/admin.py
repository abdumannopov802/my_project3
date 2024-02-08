from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(uploadVideo)
class uploadVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'islike']
    list_filter = ['title', 'islike']
    
    # readonly_fields = ('video_tag',)