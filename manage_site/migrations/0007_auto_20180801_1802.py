# Generated by Django 2.0.6 on 2018-08-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_site', '0006_auto_20180801_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['-add_time'], 'verbose_name': '轮播公告', 'verbose_name_plural': '轮播公告'},
        ),
        migrations.AlterModelOptions(
            name='preview',
            options={'ordering': ['-add_time'], 'verbose_name': '活动预告', 'verbose_name_plural': '活动预告'},
        ),
        migrations.RemoveField(
            model_name='banner',
            name='image',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='index',
        ),
        migrations.AddField(
            model_name='banner',
            name='details',
            field=models.TextField(default=1, max_length=500, verbose_name='公告内容'),
            preserve_default=False,
        ),
    ]