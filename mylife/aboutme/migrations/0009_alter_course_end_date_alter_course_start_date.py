# Generated by Django 4.1.7 on 2023-03-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0008_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]