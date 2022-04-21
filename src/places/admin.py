from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class SortableImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview_image"]
    extra = 0

    def preview_image(self, obj):
        max_height = 200
        max_width = int(
            obj.file.width / (obj.file.height / max_height)
        )  # keep original proportions
        return format_html(
            f"<img src='{obj.file.url}' width='{max_width}' height='{max_height}' />"
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [SortableImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
