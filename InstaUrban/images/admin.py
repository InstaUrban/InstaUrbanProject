from django.contrib import admin
from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'get_image',
                    'owner',
                    'city',
                    'created', )

    list_display_links = ('name',)
    list_filter = ('city',)


"""class PlaceInline(admin.TabularInline):
    model = Image
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]


admin.site.register(Image, PlaceAdmin)"""
