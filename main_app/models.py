from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import date

# Create your models here.

SPONSORS = (
    ("V", "Vic Firth"),
    ("P", "ProMark"),
    ("I", "Innovative Percussion"),
    ("Z", "Zildjian")

)

class Drum(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('drums_detail', kwargs={'pk': self.id})

class Drummer(models.Model):
    name = models.CharField(max_length=100, blank=True)
    band = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250, blank=True)
    age = models.IntegerField()
    drums = models.ManyToManyField(Drum)
    

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    stick_sponsor = models.CharField(
        max_length=1,
        choices=SPONSORS,
        default="None"
        )

    drummer = models.ForeignKey(Drummer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_stick_sponsor_display()}"