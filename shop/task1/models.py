from django.db import models
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    def __str__(self):
        return self.name
class Game(models.Model):
    title = models.CharField(max_length=100)
    cost=models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    age_limited=models.IntegerField(default=False)
    buyer=models.ManyToManyField(Buyer, related_name='game')
    def __str__(self):
        return self.title
# Create your models here.
