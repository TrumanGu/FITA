# Generated by Django 2.0.6 on 2018-07-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180718_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_member',
            field=models.BooleanField(default=False, verbose_name='是否成员'),
        ),
    ]