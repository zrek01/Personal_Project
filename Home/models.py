from django.db import models


class Contact(models.Model):
    name = models.TextField(default="Carlos Prosopio")
    number = models.TextField(default="(786) 234 - 8413")
    email = models.TextField(default='cpros003@fiu.edu')
    picture = models.ImageField(upload_to='portfolio/images/', default='')
    description = models.CharField(max_length=200, default='Web Dev - IT Tech - DB Programmer')
