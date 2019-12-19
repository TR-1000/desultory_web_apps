from django.db import models

# Create your models here.

class Url(models.Model):
    url_address = models.URLField(max_length=2083)
    url_hash = models.CharField(max_length=64)

    def __str__(self):
        return self.url_address
        return self.url_hash
