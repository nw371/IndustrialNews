from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

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

    postType = models.CharField(max_length=2, choices=TYPES, default='NS')
    postDate = models.DateField(auto_now_add=True)
    postName = models.CharField(max_length=255)
    postBody = models.TextField()
    postRating = models.SmallIntegerField(default=0)

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        post_preview = self.postBody[0:123]
        return f"{post_preview}..."

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentBody = models.TextField()
    commentDate = models.DateField(auto_now_add=True)
    commentRating = models.SmallIntegerField(default=0)

    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating -= 1
        self.save()