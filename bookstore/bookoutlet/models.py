from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=77)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # id = models.AutoField() # added automatically
    author = models.CharField(null=True,  max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True, blank=False)

    def __str__(self):
        return f'{self.title}, ({self.rating})'
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)
