import imp
from django.contrib import admin
from .models import Vote, Candidate

admin.site.register(Vote)
admin.site.register(Candidate)
