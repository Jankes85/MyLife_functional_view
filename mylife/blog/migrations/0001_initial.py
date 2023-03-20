# Generated by Django 4.1.7 on 2023-03-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('note', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(blank=True, choices=[('u', 'publiczna'), ('r', 'prywatna')], max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]