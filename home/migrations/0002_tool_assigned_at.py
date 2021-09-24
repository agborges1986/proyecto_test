# Generated by Django 3.2.6 on 2021-09-21 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='assigned_at',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_at', to='home.employee'),
            preserve_default=False,
        ),
    ]
