from django.contrib import admin

# Register your models here.
from myapp.models import Person, Movie

admin.site.register(Person)
admin.site.register(Movie)
