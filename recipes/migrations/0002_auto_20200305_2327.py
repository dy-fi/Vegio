# Generated by Django 2.2.4 on 2020-03-05 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeRequest',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='wines',
        ),
    ]
