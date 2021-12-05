from django.contrib import admin
from .models import Question,Choice

admin.site.register(Choice)
admin.site.register(Question)
admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster Admin Area'
# Register your models here.