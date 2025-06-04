"""
Admin components for tagging.
"""

from django.contrib import admin

from tagging.forms import TagAdminForm
from tagging.models import Tag
from tagging.models import TaggedItem


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm


admin.site.register(TaggedItem)
