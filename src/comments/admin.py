from django.contrib import admin

# Register your models here.
from .models import Comment


class CommenttModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "content_type", "object_id", "content_object", "parent", "content"]
    list_display_links = ["pk"]

    class Meta:
        model = Comment


admin.site.register(Comment, CommenttModelAdmin)
