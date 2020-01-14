from django.contrib import admin
from .models import User, Maincategory, Subcategory, Notice, Maincomment, Subcomment 

# Register your models here.
admin.site.register(User)
admin.site.register(Maincategory)
admin.site.register(Subcategory)
admin.site.register(Notice)
admin.site.register(Maincomment)
admin.site.register(Subcomment)