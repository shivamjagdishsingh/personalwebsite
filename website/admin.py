from django.contrib import admin
from website import models


@admin.register(models.WebDesigning)
class WebDesigningAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SoftwareDevelopment)
class SoftwareDevelopmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MachineLearning)
class MachineLearningAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonalDetail)
class PersonalDetailsAdmin(admin.ModelAdmin):
    pass



@admin.register(models.Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


