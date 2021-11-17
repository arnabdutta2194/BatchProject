from django.contrib import admin
from unesco.models import Region,Iso,State,Category,Site
# Register your models here.

admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Site)