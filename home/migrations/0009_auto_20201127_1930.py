# Generated by Django 3.1.3 on 2020-11-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201127_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabtaguzari',
            name='email',
            field=models.CharField(default='default', max_length=122),
        ),
        migrations.AlterField(
            model_name='rabtaguzari',
            name='phone',
            field=models.CharField(default='default', max_length=122),
        ),
    ]