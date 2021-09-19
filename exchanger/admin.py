from django.contrib import admin
from .models import Exchanger


class ExchangerAdmin(admin.ModelAdmin):
    list_display = ('id', 'rate', 'created_date')
    list_display_links = ('id', 'rate')
    search_fields = ('rate',)



admin.site.register(Exchanger, ExchangerAdmin)
