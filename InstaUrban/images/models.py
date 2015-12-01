from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User


class Image(models.Model):

    # Street Artist
    owner = models.ForeignKey(User, null=True, blank=True)

    # Image
    image = models.ImageField(upload_to="static/img/image_media", null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    # Location Info
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=[city], zoom=8)

    # Meta data
    created = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True
