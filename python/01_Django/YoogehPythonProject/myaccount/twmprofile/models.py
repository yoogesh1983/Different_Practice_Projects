from django.db import models
from django.urls import reverse


class Profile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField(default=18)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return 'username: ' + self.username + 'firstName: ' + self.firstName
