from django.db import models


class Post(models.Model):
    # MEDIA_ROOT/post/xxx.jpg
    photo = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
