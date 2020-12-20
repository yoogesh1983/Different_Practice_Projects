from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES=(('draft', 'Draft'), ('published', 'Published')) #Tuple inside tuple
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264, unique_for_date='publish')
    author=models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body= models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True) # when it is updated that time is taken
    updated = models.DateTimeField(auto_now=True) # when save method is called that time is taken
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        # because of this, we no need to call orderby when publish.. it will be bydefault accending..so we do reverse of it here

        # If you don't provide the comma at last, You will get the error 'ordering' must be a tuple or list (even if you want to order by
        # only one field (because there must not be a single valued tuple)
        ordering=('-publish',)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return 'title: ' + self.username + ' | author: ' + self.author

