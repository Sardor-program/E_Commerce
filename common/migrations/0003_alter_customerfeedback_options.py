# Generated by Django 5.0.6 on 2024-05-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_media_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerfeedback',
            options={'verbose_name': 'Customer feedback', 'verbose_name_plural': 'Customer feedbacks'},
        ),
    ]