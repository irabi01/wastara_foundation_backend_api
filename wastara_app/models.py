from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length = 100)
    event_date = models.DateField()
    event_time_start = models.CharField(max_length = 10)
    event_time_finish = models.CharField(max_length = 10)
    location = models.CharField(max_length = 50, default ='Morogoro')
    date = models.DateTimeField(auto_now_add =True)
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    body = models.TextField()
    sponsor = models.CharField(max_length = 200)
    class Meta:
        verbose_name_plural = "Event Data"
    def __str__(self):
        return self.title
