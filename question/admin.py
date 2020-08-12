from django.contrib import admin

# Register your models here.

from .models import Tag, Question
from django.contrib.auth.models import User

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name",               {'fields': ['name']}),
        ("Status",             {'fields': ['status']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'status')
    list_display_links = ('name', 'status')
    list_filter = ('name', 'status')

admin.site.register(Tag,TagAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('status','title','user','pub_date')
    list_display_links = ('status','title')
    list_filter = ('status','title','desc')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Question,QuestionAdmin)
