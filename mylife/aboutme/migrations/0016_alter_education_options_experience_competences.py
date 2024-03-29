# Generated by Django 4.1.7 on 2023-03-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0015_remove_book_recomendation_book_competences'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end_date'], 'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
        migrations.AddField(
            model_name='experience',
            name='competences',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
