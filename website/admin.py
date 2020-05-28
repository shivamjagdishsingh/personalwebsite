from django.contrib import admin
from website import models

admin.site.site_header = 'Shivam World'

admin.site.register(models.WebDesigning)
admin.site.register(models.SoftwareDevelopment)
admin.site.register(models.MachineLearning)
admin.site.register(models.PersonalDetail)
admin.site.register(models.Skill)
admin.site.register(models.Experience)
