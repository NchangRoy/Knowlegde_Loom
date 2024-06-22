from django.contrib import admin
from .models import Classes,Topics,Subjects,subtopic,image
admin.site.register(Classes)
admin.site.register(Subjects)
admin.site.register(Topics)
admin.site.register(subtopic)
admin.site.register(image)
# Register your models here.
