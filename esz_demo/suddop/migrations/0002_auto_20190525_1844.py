# Generated by Django 2.2 on 2019-05-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suddop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='ApplicantSnils',
            field=models.CharField(max_length=11, null=True, verbose_name='СНИЛС'),
        ),
    ]