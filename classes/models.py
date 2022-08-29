from django.db import models

# Create your models here.
class playerModel(models.Model):
    player_class = models.CharField(max_length=100)
    player_subclass = models.CharField(max_length=100)
    abreviation = models.CharField(max_length=100)
    equipments = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    constituition = models.CharField(max_length=100)
    dexterity = models.CharField(max_length=100)
    intelligence = models.CharField(max_length=100)
    wisdom = models.CharField(max_length=100)
    charisma = models.CharField(max_length=100)
