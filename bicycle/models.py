from django.db import models


class Bicycle(models.Model):

    brand = models.CharField(max_length=85, blank=True, null=True)
    serial = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand
