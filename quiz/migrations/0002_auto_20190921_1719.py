# Generated by Django 2.2.4 on 2019-09-21 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='answer',
            table='answers',
        ),
        migrations.AlterModelTable(
            name='question',
            table='questions',
        ),
    ]