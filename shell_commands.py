from django.contrib.auth.models import User
from django.db import models
from news.models import Author
from news.models import Category
from news.models import Post
from news.models import PostCategory
from news.models import Comment


user1 = User.objects.create_user(username="UserName1", password="UN1pass")
user2 = User.objects.create_user(username="UserName2", password="UN2pass")

author1 = Author.objects.create(author=user1)
author2 = Author.objects.create(author=user2)

cat1 = Category.objects.create(name='Микроэлектроника')
cat2 = Category.objects.create(name='Робототехника')
cat3 = Category.objects.create(name='Софт')
cat4 = Category.objects.create(name='Промышленность 4.0')