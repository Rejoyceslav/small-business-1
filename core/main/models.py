from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Materialy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='materialy_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']  # when ordering multiple values, this is the order


class Uslugi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
