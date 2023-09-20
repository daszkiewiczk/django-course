from django.db import models

class UserModel(models.Model):
    # user_image = models.FileField()
    user_image = models.ImageField(upload_to='images')