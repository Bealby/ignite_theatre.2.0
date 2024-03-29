from django.db import models
'''Pillow must be installed'''


class Show(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    gallery_show_link = models.CharField(max_length=254)
    poster = models.ImageField(null=True, blank=True)
    testimonial_1 = models.CharField(max_length=254, null=True, blank=True)
    testimonial_2 = models.CharField(max_length=254, null=True, blank=True)
    testimonial_3 = models.CharField(max_length=254, null=True, blank=True)
    testimonial_4 = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Actor(models.Model):

    class Meta:
        verbose_name_plural = 'Actors'
    '''null=True, blank=True are optional fields'''

    show = models.ForeignKey('show', null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    website = models.CharField(max_length=254, null=True, blank=True)
    facebook = models.CharField(max_length=254, null=True, blank=True)
    film = models.CharField(max_length=254, null=True, blank=True)
    position = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Crew(models.Model):

    show = models.ForeignKey('show', null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    position = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Cast(models.Model):

    show = models.ForeignKey('show', null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    position = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
