from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class SortableImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview_image"]
    extra = 0
    fields = ("file", "preview_image", "order")

    def preview_image(self, obj):
        return format_html(
            f"<img src='{obj.file.url}' style='max-height:200px;max-width:400px' />"
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [SortableImageInline]
    ordering = ["title"]
    search_fields = ["title"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
