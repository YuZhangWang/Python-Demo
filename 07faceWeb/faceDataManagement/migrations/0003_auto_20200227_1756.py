# Generated by Django 3.0.3 on 2020-02-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceDataManagement', '0002_auto_20200227_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name_picture',
            name='picture',
            field=models.CharField(max_length=65532, verbose_name='picture'),
        ),
    ]