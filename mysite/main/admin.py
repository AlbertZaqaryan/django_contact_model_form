from django.contrib import admin
from .models import Phone, About, Contact
# Register your models here.


admin.site.register(Phone)
admin.site.register(About)


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_email']
    list_display_links = ['id', 'user_name']
    search_fields = ['user_name', 'user_email', 'user_phone']