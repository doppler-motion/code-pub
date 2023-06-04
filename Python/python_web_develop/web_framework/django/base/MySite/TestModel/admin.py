from django.contrib import admin

from TestModel.models import MyModelDb, Contact, Tag

# Register your models here.
admin.site.register([MyModelDb, Contact, Tag])
