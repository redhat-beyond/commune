from django.contrib import admin
from .models import Chore, User, Vote, Commune


admin.site.register(Chore)
admin.site.register(User)
admin.site.register(Vote)
admin.site.register(Commune)
