from django.contrib import admin

# Register your models here.

from .models import Tag, Question
from django.contrib.auth.models import User

# class TagAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Name",               {'fields': ['name']}),
#         ("Status",             {'fields': ['status']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     list_display = ('name', 'status')
#     list_display_links = ('name', 'status')
#     list_filter = ('name', 'status')

# admin.site.register(Tag,TagAdmin)

# class UserInline(admin.TabularInline):
#     model = User

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Title", {'fields': ['title']}),
#         ("Desc", {'fields': ['desc']}),
#         ("Status",             {'fields': ['status']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     list_display = ('status','title')
#     list_display_links = ('status','title')
#     list_filter = ('status','title')
#     inlines = (UserInline,)


# admin.site.register(Question,QuestionAdmin)
