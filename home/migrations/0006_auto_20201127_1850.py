# Generated by Django 3.1.3 on 2020-11-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201127_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabtaguzari',
            name='phone',
            field=models.CharField(max_length=122),
        ),
    ]