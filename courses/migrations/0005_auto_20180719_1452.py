# Generated by Django 2.0.6 on 2018-07-19 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180717_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseresource',
            name='course',
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['start_time'], 'verbose_name': '章节', 'verbose_name_plural': '章节'},
        ),
        migrations.DeleteModel(
            name='CourseResource',
        ),
    ]