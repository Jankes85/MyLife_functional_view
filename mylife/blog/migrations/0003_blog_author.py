# Generated by Django 4.1.7 on 2023-03-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_creation_time_blog_entry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='me', max_length=30),
            preserve_default=False,
        ),
    ]
