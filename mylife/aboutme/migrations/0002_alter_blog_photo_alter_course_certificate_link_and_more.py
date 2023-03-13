# Generated by Django 4.1.7 on 2023-03-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='certificate_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_level',
            field=models.CharField(blank=True, choices=[('b', 'Basic'), ('a', 'Advanced'), ('i', 'Intermediate'), ('j', 'Junior'), ('m', 'Mid'), ('s', 'Senior')], max_length=1),
        ),
    ]