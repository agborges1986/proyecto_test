# Generated by Django 3.2.6 on 2021-10-29 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_user_id'),
        ('home', '0009_alter_certification_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='created_for',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='certification_created_for', to='login.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='approved_for',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_approved', to='login.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tool',
            name='created_for',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tool_created_for', to='login.user'),
            preserve_default=False,
        ),
    ]
