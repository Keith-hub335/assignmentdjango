from collections import Counter

from django.contrib import admin



from Admin.models import Announcements, Trainers, Courses

# Register your models here.
admin.site.register(Courses)
admin.site.register(Trainers)
admin.site.register(Announcements)