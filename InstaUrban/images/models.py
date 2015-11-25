from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User


class Place(models.Model):

    # Street Artist
    owner = models.ForeignKey(User, null=True, blank=True)

    # Image
    image = models.ImageField(upload_to="static/img/place_media", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # Location Info
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=[city], zoom=8)

    # Meta data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
