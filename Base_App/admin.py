from django.contrib import admin
from Base_App.models import *
from .models import Cake
# Register your models here.
admin.site.register(Cake)
admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
