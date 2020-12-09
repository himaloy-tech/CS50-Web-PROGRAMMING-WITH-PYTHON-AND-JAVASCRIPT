from django.contrib import admin
from .models import Listings, User, Watchlist
# Register your models here.

class ListingsAdmin(admin.ModelAdmin):
    list_display = ("title", "category")

class WatchlistAdmin(admin.ModelAdmin):
    filter_horizontal = ("products",) 

admin.site.register(Listings, ListingsAdmin)
admin.site.register(User)
admin.site.register(Watchlist, WatchlistAdmin)