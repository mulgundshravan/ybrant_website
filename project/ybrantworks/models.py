from django.db import models

# Create your models here.
class Ybrantworks(models.Model):
    image=models.ImageField(upload_to="image/")
    summary=models.TextField()