from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Users"
