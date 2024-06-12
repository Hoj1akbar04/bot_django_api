from django.contrib import admin
from .models import Users, Product
#

admin.site.register([Users, Product])