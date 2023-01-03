from django.contrib import admin

from .models import Family, Charity, Business, Culture, Book_event, Contact_us

# Register your models here.
admin.site.register(Family)
admin.site.register(Charity)
admin.site.register(Business)
admin.site.register(Culture)
admin.site.register(Book_event)
admin.site.register(Contact_us)
