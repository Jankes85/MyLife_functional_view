from django.contrib import admin
from . import models

# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    list_display = ("school_name", "course_name", "blocks", "start_date", "end_date", "degree")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("school_name", "course_name", "start_date", "end_date", "certificate")


class BookAdmin(admin.ModelAdmin):
    list_display = ("author_name", "title", "end_date", "recomendation")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "technologies", "repository")


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "workplace", "start_date", "end_date", "duties")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_type", "skill_level")


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language_name", "language_level")


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "note", "creation_datetime", "photo")

admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Blog, BlogAdmin)
