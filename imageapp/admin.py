from django.contrib import admin
from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", 
                    "created_time", "slug", 
                    "url", "user", "created_time", 
                    )
    list_filter = ("user", "created_time")
    search_fields = ("user",)
    fieldsets = (
        ("user and followers", {"fields": ("user", "user_like")}),
        ("image info", {"fields": ("title", "slug", "description")}),
        ("image location", {"fields": ("url", "image",)}),
    )
    


admin.site.register(Image, ImageAdmin)