# Generated by Django 3.2.5 on 2021-07-28 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newmovie', '0003_auto_20210727_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newmovie.movie'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newmovie.usermine'),
        ),
    ]
