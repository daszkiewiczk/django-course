from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email_address = models.EmailField(blank=True, max_length=100)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=100)
    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=1000)
    # image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[
        MinLengthValidator(10),
    ])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    author = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    content = models.TextField(max_length=1000, validators=
                               [
                                   MinLengthValidator(10),
                               ])
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=False)
