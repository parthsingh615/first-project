from django.contrib import admin

# Register your models here.
from django.contrib import admin
from gnoida.models import main
from gnoida.models import to_approve
admin.site.register(main)
admin.site.register(to_approve)