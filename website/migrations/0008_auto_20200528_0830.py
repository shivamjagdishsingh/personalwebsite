# Generated by Django 2.2 on 2020-05-28 08:30

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200528_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinelearning',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=website.models.get_upload_path),
        ),
    ]
