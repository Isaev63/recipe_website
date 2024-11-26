from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User


class RecipeModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipe/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def short_description(self):
        return Truncator(self.description).words(12, truncate='...')
