from django.contrib import admin


# Register your models here.

from .models import Trabajo
from .models import Contacter

admin.site.register(Trabajo)
admin.site.register(Contacter)
