from django.contrib import admin

# Register your models here.

from .models import Review, ContactMessage, CourseMaterial

admin.site.register(ContactMessage)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'rating', 'approved')
    list_filter = ('approved', 'rating')
    search_fields = ('text', 'user__username')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True) # What is request here for?
    approve_reviews.short_description = "Zatwierdź wybrane opinie"


@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'order')
    list_filter = ('subject',)
    search_fields = ('topic',)
    ordering = ('subject', 'order')