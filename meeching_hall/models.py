from django.db import models
'''Pillow must be installed'''


class MeechingHall(models.Model):
    '''Programmatic Name'''

    name = models.CharField(max_length=254)
    ideas_url = models.CharField(max_length=254, null=True, blank=True)
    ideas_image = models.ImageField(blank=True)
    memories_url = models.CharField(max_length=254, null=True, blank=True)
    memories_image = models.ImageField(blank=True)
    petition_url = models.CharField(max_length=254, null=True, blank=True)
    petition_image = models.ImageField(blank=True)
    meeching_hall_content = models.TextField(max_length=2000, null=True, blank=True)
    meeching_hall_image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
