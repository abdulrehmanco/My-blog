# Generated by Django 3.1.3 on 2020-11-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201129_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='sno',
            field=models.AutoField(default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]