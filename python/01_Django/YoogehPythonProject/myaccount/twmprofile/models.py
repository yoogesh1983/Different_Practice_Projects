from django.db import models
from django.urls import reverse


class CustomManager(models.Manager):

    # Profile.objects.all() internally calls get_queryset() mehtod. we are here overriding that method
    def get_queryset(selfs):
        return super().get_queryset().order_by('firstName')

    def getProfileWithAgeRange(self, age1, age2):
        return super().get_queryset().filter(age__range=[age1, age2])


class Profile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    objects = CustomManager() # if you put 'yms' instead of 'objects', you need to use Profile.yms.all() instead of Profile.objects.all() to get all profiles

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return 'username: ' + self.username + 'firstName: ' + self.firstName

