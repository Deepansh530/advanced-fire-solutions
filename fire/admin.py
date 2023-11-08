from django.contrib import admin
from .models import Staff, Review, ContactMessage

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'post',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'review',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message',)
