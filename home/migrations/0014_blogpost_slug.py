# Generated by Django 3.1.3 on 2020-11-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
