from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()


def __str__(self):
    return 'username: ' + self.username + 'firstName: ' + self.firstName
