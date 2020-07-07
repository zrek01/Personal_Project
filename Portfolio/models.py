from django.db import models

# Create your models here.
class Resume(models.Model):
    image = models.FileField(upload_to='portfolio/images/')
