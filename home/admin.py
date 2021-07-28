from django.contrib import admin
from .models import User, Qsmart, Remarks, Suggestion

# Register your models here.
admin.site.register(User)
admin.site.register(Qsmart)
admin.site.register(Remarks)
admin.site.register(Suggestion)
