from django.db import models
from django.utils import timezone
# from django.utils.html import mark_safe

# Create your models here.

class uploadVideo(models.Model):
    title = models.CharField(max_length = 30)
    video = models.FileField(upload_to='videos_uploaded')
    islike = models.BooleanField(default = False)
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
    
    # def image_tag(self):
    #     return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    # image_tag.short_description = 'Image'
