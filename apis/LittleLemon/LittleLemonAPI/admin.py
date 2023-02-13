from django.contrib import admin
from .models import *

# Register your models here.

admin.register(Category)
admin.register(MenuItem)
admin.register(Cart)
admin.register(Order)
admin.register(OrderItem)
