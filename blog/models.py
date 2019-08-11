from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.

class BlogPosts(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    post_content = MarkdownxField(max_length=99999)
    date_posted = models.DateTimeField(auto_now_add=True, editable=False)
