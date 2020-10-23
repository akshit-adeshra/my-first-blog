from django.contrib import admin, messages
from .models import Post, Comment
# Register your models here.
@admin.register(Post)               # This command is the alternative of the command written on line 24 i.e. admin.site.register(Post, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'category', 'title', 'text', 'created_date', 'published_date')

    fieldsets = (
        (None, {
            'fields': ('author','category','title','text','reference')
        }),
        ('Timings', {
            'fields': ('created_date','published_date')
        }),
    )

    def active(self, obj):
        return obj.is_active == 1
    
    active.boolean = True

    def make_active(self, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected record(s) made active..!!")

    def make_inactive(self, modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected record(s) made Inactive..!!")

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")

# admin.site.register(Post, PostAdmin)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('post','text','author','created_date','approved_comment')
    list_filter = ('post','approved_comment')