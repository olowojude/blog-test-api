from django.db import models


class BlogPosts(models.Model):
    name = models.CharField(max_length=200)
    post = models.TextField()

    def __str__(self):
        return self.name