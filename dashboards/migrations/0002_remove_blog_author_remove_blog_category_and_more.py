# Generated by Django 5.0.6 on 2024-06-15 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
