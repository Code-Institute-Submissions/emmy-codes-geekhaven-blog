from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import render


PUBLISHED_STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    blog_heading = models.CharField(max_length=250, unique=True)
    heading_image = CloudinaryField("image", default="placeholder")
    url_slug = models.SlugField(max_length=250, unique=True, blank=True)
    blog_published_status = models.IntegerField(
        choices=PUBLISHED_STATUS,
        default=0
    )
    blog_content = models.TextField(default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    content_updated_on = models.DateTimeField(auto_now_add=True)

    # stores ref to the User that is the author of the post.
    blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # blank=True means the field is not required
    blog_likes = models.ManyToManyField(
        User,
        related_name="blog_likes",
        blank=True
    )

    # to give a preview text on the post icons on the main page
    blog_excerpt = models.TextField(default="", blank=True)

    class Meta:
        ordering = ["-creation_date"]

    # changes object name on admin site to blog_heading of blog
    def __str__(self):
        return self.blog_heading


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
