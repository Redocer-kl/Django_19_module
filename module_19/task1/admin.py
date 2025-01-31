from django.contrib import admin
from .models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    search_fields = ('title',)
    list_per_page = 20

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance',  'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)

admin.site.register(Game, GameAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(News, NewsAdmin)