# Generated by Django 3.2.8 on 2021-10-11 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Student_List'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student_Table',
        ),
    ]
