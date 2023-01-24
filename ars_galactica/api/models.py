from django.db import models


class Paintings(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.CharField(max_length=255)
    year = models.IntegerField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
