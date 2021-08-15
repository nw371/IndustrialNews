from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(Author=self.author).values('post_rating')



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Post(models.Model):
    news = 'NS'
    article = 'AL'
    TYPES = [
        (news,'Новость'),
        (article,'Статья')
    ]

    post_type = models.CharField(max_length=2, choices=TYPES, default='NS')
    post_date = models.DateField(auto_now_add=True)
    post_name = models.CharField(max_length=255)
    post_body = models.TextField()
    post_rating = models.IntegerField(default=0)

    post = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        post_preview = self.post_body[:124]
        return f"{post_preview}..."

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()