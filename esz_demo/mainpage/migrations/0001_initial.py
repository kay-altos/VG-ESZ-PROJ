# Generated by Django 2.2 on 2019-04-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SitePropertis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=30)),
                ('property_data', models.CharField(max_length=30)),
            ],
        ),
    ]