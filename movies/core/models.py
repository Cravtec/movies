from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices

AGE_CHOICES = Choices(
    (0, 'kids', 'kids'),
    (1, 'teens', 'teens'),
    (2, 'adults', 'adults'),
)


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null=True, blank=True, choices=AGE_CHOICES)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('name', 'last_name')

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(null=True,
                                 validators=[MaxValueValidator(10),
                                             MinValueValidator(1)])
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)
    director = models.ForeignKey(Director, null=True, on_delete=models.DO_NOTHING)
    country = models.ManyToManyField(Country, related_name='movies')

    class Meta:
        unique_together = ('title', 'released')

    def __str__(self):
        return f"{self.title} from {self.released}"
