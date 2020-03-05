# Generated by Django 2.2.4 on 2020-02-28 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoon_id', models.CharField(max_length=300)),
                ('title', models.CharField(help_text='Recipe Title', max_length=300)),
                ('summary', models.TextField(help_text='Recipe Summary')),
                ('image_url', models.CharField(max_length=400)),
                ('wines', models.CharField(help_text='Wines that pair the best with the recipe', max_length=600)),
                ('source_url', models.CharField(help_text='Recipe Url', max_length=300)),
                ('slug', models.CharField(blank=True, editable=False, help_text='URL to find this recipe', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this page was created. Automatically generated when the model saves.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Recipe name...', max_length=200)),
            ],
        ),
    ]