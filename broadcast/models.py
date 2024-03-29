from django.db import models
from movie.models import Movie
from hall.models import Hall

# Create your models here.
class Broadcast(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    beginTime = models.CharField(max_length=20)
    endTime = models.CharField(max_length=20)
    seats = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)