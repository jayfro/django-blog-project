from django.db import models

# Create your models here.


class Post(models.Model):

    title=models.CharField(max_length = 70)

    body=models.TextField()

    created=models.DateField()
    updated=models.DateField()

class Comment(models.Model):

    body=models.TextField()

    author=models.CharField(max_length=70)

    created=models.DateField()
    updated=models.DateField()

    post=models.ForeignKey(Post,related_name = 'Post')

    
  

    
