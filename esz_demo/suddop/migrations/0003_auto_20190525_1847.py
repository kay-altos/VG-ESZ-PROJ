# Generated by Django 2.2 on 2019-05-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suddop', '0002_auto_20190525_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='ApplicantSnils',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='СНИЛС'),
        ),
    ]