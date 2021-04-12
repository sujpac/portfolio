from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50, default='Job Title')
    summary = models.CharField(max_length=200)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.summary[:10]
