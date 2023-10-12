from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


