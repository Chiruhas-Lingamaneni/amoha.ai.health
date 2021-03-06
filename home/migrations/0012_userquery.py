# Generated by Django 3.1.5 on 2021-04-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210206_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('mobileNumber', models.IntegerField(max_length=11)),
                ('organisation', models.CharField(max_length=80)),
                ('message', models.TextField()),
            ],
        ),
    ]
