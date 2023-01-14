from django.db import models
'''Pillow must be installed'''


class Show(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254, null=True, blank=True)
    date = models.CharField(max_length=254, null=True, blank=True)
    ticket_retail_image = models.ImageField(null=True, blank=True)
    ticket_retail_name = models.CharField(max_length=254, null=True,
                                          blank=True)
    ticket_retail_url = models.CharField(max_length=254, null=True, blank=True)
    ticket_retail_address = models.TextField(max_length=400, null=True,
                                             blank=True)
    sponsor_image = models.ImageField(null=True, blank=True)
    sponsor_name = models.CharField(max_length=254, null=True, blank=True)
    sponsor_url = models.CharField(max_length=254, null=True, blank=True)
    show_poster = models.ImageField(null=True, blank=True)
    show_content = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Upcoming(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254, null=True, blank=True)
    date = models.CharField(max_length=254, null=True, blank=True)
    location_2 = models.CharField(max_length=254, null=True, blank=True)
    date_2 = models.CharField(max_length=254, null=True, blank=True)
    location_3 = models.CharField(max_length=254, null=True, blank=True)
    date_3 = models.CharField(max_length=254, null=True, blank=True)
    position = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
