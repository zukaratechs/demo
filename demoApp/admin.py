from django.contrib import admin

# Register your models here.
from demoApp.models import Owner, Dog, Cat

admin.site.register(Owner)
admin.site.register(Dog)
admin.site.register(Cat)