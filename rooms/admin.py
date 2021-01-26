from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "contury",
                    "address",
                    "price",
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "More About The Space",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "Facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    ordering = (
        "name",
        "price",
        "bedrooms",
    )

    list_display = (
        "name",
        "description",
        "contury",
        "city",
        "price",
        "guests",
        "beds",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "Facilities",
        "house_rules",
        "city",
        "contury",
    )

    search_fields = ("city", "^host__username")

    filter_horizontal = (
        "amenities",
        "Facilities",
        "house_rules",
    )

    def count_amenities(self, obj):

        return "potato"

    count_amenities.short_description = "hello"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
