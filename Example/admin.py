from django.contrib import admin
from .models import Example


class ExampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descriptions', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'descriptions')
    # list_editable = 'title'  # Edit without log in the model
    list_filter = 'date'


admin.register(Example, ExampleAdmin)
