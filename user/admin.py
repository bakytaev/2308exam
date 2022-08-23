from django.contrib import admin
from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'main_work', 'phone_number', 'get_level')

    @admin.display(description='Level')
    def get_level(self, obj):
        if 2022 - obj.experience.year > 3:
            return 'middle'
        else:
            return 'strong junior'


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date_started',)


# Register your models here.
admin.site.register(Language)
admin.site.register(Student)
# admin.site.register(Mentor)
admin.site.register(Course)
