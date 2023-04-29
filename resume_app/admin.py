from django.contrib import admin
from .models import *

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Candidate._meta.get_fields()]


admin.site.register(Candidate,CandidateAdmin)
