from django.db import models
'''Pillow must be installed'''


class NewShow(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    date = models.CharField(max_length=254)
    image_ticket = models.ImageField(null=True, blank=True)
    web_ticket = models.CharField(max_length=254)
    address_ticket = models.TextField(max_length=254)
    image_sponsor = models.ImageField(null=True, blank=True)
    image_show = models.ImageField(null=True, blank=True)
    content_show = models.TextField(max_length=254)

    def __str__(self):
        return self.name


class UpcomingShow(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
