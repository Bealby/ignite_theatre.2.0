from django.db import models
'''Pillow must be installed'''


class MeechingHall(models.Model):
    '''Programmatic Name'''

    name = models.CharField(max_length=254)
    meeching_hall_petition = models.CharField(max_length=254, null=True, blank=True)
    meeching_hall_image = models.ImageField(blank=True)
    meeching_hall_content = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name
