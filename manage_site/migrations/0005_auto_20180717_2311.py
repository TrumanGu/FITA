# Generated by Django 2.0.6 on 2018-07-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_site', '0004_auto_20180715_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexcoremembers',
            name='image',
            field=models.ImageField(upload_to='manage_site/member/%Y/%', verbose_name='成员照片'),
        ),
        migrations.AlterField(
            model_name='indexcourse',
            name='img',
            field=models.ImageField(max_length=200, upload_to='manage_site/course/%Y/%m', verbose_name='课程LOGO'),
        ),
        migrations.AlterField(
            model_name='indeximgshow',
            name='image',
            field=models.ImageField(upload_to='manage_site/img_show/%Y/%d', verbose_name='照片'),
        ),
    ]
