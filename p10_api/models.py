from django.db import models

# Create your models here.
class P10Status(models.Model):
    device_name = models.CharField(max_length=200)
    device_message = models.CharField(max_length=200)
    device_brightness=models.IntegerField()
    device_scrolling_speed=models.IntegerField()

    def __str__(self):
        return self.device_name


