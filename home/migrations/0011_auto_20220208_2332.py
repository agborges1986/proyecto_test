# Generated by Django 3.2.6 on 2022-02-09 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211029_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves_employee_tools', to='home.employee'),
        ),
        migrations.AlterField(
            model_name='move',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tool_moved', to='home.tool'),
        ),
    ]
