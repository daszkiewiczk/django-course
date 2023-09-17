from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

class Address(models.Model):
    street = models.CharField(max_length=77)
    postal_code = models.CharField(max_length=77)
    city = models.CharField(max_length=77)
    def __str__(self):
        return f'{self.street}, {self.city}'
    
    class Meta:
        verbose_name_plural = "Address Entries" 

class Author(models.Model):
    first_name = models.CharField(max_length=77)
    last_name = models.CharField(max_length=77)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=77)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # id = models.AutoField() # added automatically
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', editable=True, null=False, db_index=True, blank=True)
    published_countries = models.ManyToManyField(Country)
    def __str__(self):
        return f'{self.title}, ({self.rating})'
    

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
