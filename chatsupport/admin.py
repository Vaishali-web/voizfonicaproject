from django.contrib import admin
from .models import Ticket,Chat,Messages

# Register your models here.

admin.site.register(Chat)
admin.site.register(Ticket)
admin.site.register(Messages)
