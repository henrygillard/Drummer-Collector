from django.db import models

# Create your models here.
class Drummer:
    def __init__(drummer, name, band, description, age, sponsor):
        drummer.name = name
        drummer.band = band
        drummer.description = description
        drummer.age = age
        drummer.sponsor = sponsor

drummers = [
    Drummer("Chris Coleman", "Beck", "Mainly a solo artist, Chris also plays for Beck.", 38, "Meinl"),
    Drummer("Tommy Igoe", "Tommy Igoe Big Band", "Tommy is the creator the Groove Essentials, wrote the drum book for the Lion King musical, and has over 60,000 followers on social media", 56, "Vic Firth"),
    Drummer("Niel Peart", "Rush", "Niel Peart is considered a drumming legend, may he RIP", 67, "Remo"),
]

