from django.contrib import admin

from .models import *

admin.site.register(UserMine)
admin.site.register(Movie)
admin.site.register(Order)
admin.site.register(Tag)