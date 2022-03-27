# Generated by Django 3.2.5 on 2021-07-28 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newmovie', '0004_auto_20210728_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(default=django.utils.timezone.now, upload_to='video/'),
            preserve_default=False,
        ),
    ]
