from django.db import models
from django.urls import reverse

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name} - {self.address}'

class Participant(models.Model):
    email = models.EmailField(unique=True) 
    

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Participant_detail", kwargs={"pk": self.pk})

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(default='orga@niz.er')
    date = models.DateField(default='2021-01-01')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
 