from django.db import models
'''Pillow must be installed'''


class Show(models.Model):

    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Ticket(models.Model):

    show = models.ForeignKey('show', null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    event_date = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    place = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    position = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price_details = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    web = models.CharField(max_length=254, null=True, blank=True)
    adult_price = models.DecimalField(max_digits=8, decimal_places=2,
                                      null=True, blank=True)
    child_price = models.DecimalField(max_digits=8, decimal_places=2,
                                      null=True, blank=True)

    def __str__(self):
        return self.name
