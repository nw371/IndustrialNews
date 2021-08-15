# from django.contrib.auth.models import User
# from django.db import models


from news.models import *
# from news.models import Author
# from news.models import Category
# from news.models import Post
# from news.models import PostCategory
# from news.models import Comment
import random

ptype = ['AL','NS']
aindex = [1,2]
usersQTY = 10
authQTY = 2
postQTY = 15
commQTY = 25
catQTY = 4

for n in range(0, catQTY):
    globals()[f'cat{n}'] = Category.objects.create(name=f'Category{n}')

for n in range(0, usersQTY):
    globals()[f'user{n}'] = User.objects.create_user(username=f"UserName{n}", password=f"UN{n}pass")

for n in range(0, 2):
    globals()[f'author{n}'] = Author.objects.create(author=globals()[f'user{n}'])

for n in range(0, postQTY):
    globals()[f'post{n}'] = Post.objects.create(postType=f'{random.choice(ptype)}',
                                postName=f'Post {n} Name',
                                postBody=f'Very long post Nr.{n} body created for tests just to fill database. '
                                         f'it will be longer, than 124 characters, to make sure - preview '
                                         f'method does the job. It does not need to have any meaning. '
                                         f'Just ID1 to make sure this post belongs to Post {n}',
                                postAuthor=Author.objects.get(id=random.choice(aindex)),
                                )
for n in range(0, commQTY):
    globals()[f'comment{n}'] = Comment.objects.create(post=globals()[f'post{random.choice(range(0,postQTY-1))}'],
                                                      user=globals()[f'user{random.choice(range(0,usersQTY-1))}'],
                                                      commentBody=f'Generated comment {n} body.')



# user1 = User.objects.create_user(username="UserName1", password="UN1pass")
# user2 = User.objects.create_user(username="UserName2", password="UN2pass")
# user3 = User.objects.create_user(username="UserName3", password="UN3pass")
# user4 = User.objects.create_user(username="UserName4", password="UN4pass")
# user5 = User.objects.create_user(username="UserName5", password="UN5pass")
# user6 = User.objects.create_user(username="UserName6", password="UN6pass")
#
# author1 = Author.objects.create(author=user1)
# author2 = Author.objects.create(author=user2)
#
# cat1 = Category.objects.create(name='Микроэлектроника')
# cat2 = Category.objects.create(name='Робототехника')
# cat3 = Category.objects.create(name='Софт')
# cat4 = Category.objects.create(name='Промышленность 4.0')
#
# post1 = Post.objects.create(postType='AL',
#                             postName='Article 1 Name',
#                             postBody='very long post body created for tests just to fill database. '
#                                       'it will be longer, than 124 characters, to make sure - preview '
#                                       'method does the job. It does not need to have any meaning. '
#                                       'Just ID1 to make sure this post belongs to Article 1',
#                             postAuthor=Author.objects.get(id=1),
#                             )
# post2 = Post.objects.create(postType='AL',
#                             postName='Article 2 Name',
#                             postBody='very long post body created for tests just to fill database. '
#                                       'it will be longer, than 124 characters, to make sure - preview '
#                                       'method does the job. It does not need to have any meaning. '
#                                       'Just ID1 to make sure this post belongs to Article 2',
#                             postAuthor=Author.objects.get(id=1),
#                             )
# post3 = Post.objects.create(postType='AL',
#                             postName='Article 3 Name',
#                             postBody='very long post body created for tests just to fill database. '
#                                       'it will be longer, than 124 characters, to make sure - preview '
#                                       'method does the job. It does not need to have any meaning. '
#                                       'Just ID1 to make sure this post belongs to Article 3',
#                             postAuthor=Author.objects.get(id=1),
#                             )
# post4 = Post.objects.create(postType='NS',
#                             postName='News 4 Name',
#                             postBody='very long post body created for tests just to fill database. '
#                                       'it will be longer, than 124 characters, to make sure - preview '
#                                       'method does the job. It does not need to have any meaning. '
#                                       'Just ID1 to make sure this post belongs to News 4',
#                             postAuthor=Author.objects.get(id=1),
#                             )
# post5 = Post.objects.create(postType='NS',
#                             postName='News 5 Name',
#                             postBody='very long post body created for tests just to fill database. '
#                                       'it will be longer, than 124 characters, to make sure - preview '
#                                       'method does the job. It does not need to have any meaning. '
#                                       'Just ID1 to make sure this post belongs to News 5',
#                             postAuthor=Author.objects.get(id=2),
#                             )
#
# comment1 = Comment.objects.create(post=post1, user=user1, commentBody='Comment 1 body.')
# comment2 = Comment.objects.create(post=post1, user=user3, commentBody='Comment 2 body.')
# comment3 = Comment.objects.create(post=post2, user=user4, commentBody='Comment 3 body.')
# comment4 = Comment.objects.create(post=post3, user=user2, commentBody='Comment 4 body.')
# comment5 = Comment.objects.create(post=post3, user=user1, commentBody='Comment 5 body.')
# comment6 = Comment.objects.create(post=post4, user=user1, commentBody='Comment 6 body.')
# comment7 = Comment.objects.create(post=post4, user=user1, commentBody='Comment 7 body.')
# comment8 = Comment.objects.create(post=post1, user=user1, commentBody='Comment 8 body.')
# comment9 = Comment.objects.create(post=post1, user=user1, commentBody='Comment 9 body.')
# comment10 = Comment.objects.create(post=post2, user=user1, commentBody='Comment 10 body.')