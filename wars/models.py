from django.db import models

# Create your models here.

class War(models.Model):
    name = models.CharField(max_length=200)
    major_players = models.CharField(max_length=1000)
    key_technologies = models.CharField(max_length=500)
    winner = models.CharField(max_length=500)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Battle(models.Model):
    war = models.ForeignKey(War, on_delete=models.CASCADE, related_name='battles')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    major_players = models.CharField(max_length=1000)
    key_technologies = models.CharField(max_length=500)
    winner = models.CharField(max_length=500)

    def __str__(self):
        return self.name