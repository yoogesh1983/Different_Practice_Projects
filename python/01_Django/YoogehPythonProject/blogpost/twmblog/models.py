from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))  # Tuple inside tuple
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264, unique_for_date='publish')  # It is used to build SEO friendly URL
    # related_name is useful when we require all Post related to the User. Just becasue of this, all the posts also comes whenever you search for user
    # Similarly, on_delete=models.CASCADE says whenever the User is deleted, all the posts associated to that User should also be deleted
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # everytime the post object is updated that time is taken
    updated = models.DateTimeField(auto_now=True)  # when save method is called that time is taken
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = CustomManager()
    tags = TaggableManager(blank=True) # Third party application 'tagging' which is used for tagging purpose i.e we should use Post.tags.all() for this

    class Meta:
        # because of this, we no need to call orderby when publish.. it will be bydefault accending..so we do reverse of it here

        # If you don't provide the comma at last, You will get the error 'ordering' must be a tuple or list (even if you want to order by
        # only one field (because there must not be a single valued tuple)
        ordering = ('-publish',)

    def __str__(self):
        return 'title: ' + self.title + ' | author: ' + self.status

    def get_absolute_url(self):
        # return reverse('detail',kwargs={'pk':self.pk})
        return reverse('detail',
                       args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])


class EmailForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    to = models.EmailField()
    comments = models.CharField(max_length=300)


class Comment(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Commented By {} on {}'.format(self.name, self.post)
