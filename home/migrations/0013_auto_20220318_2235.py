# Generated by Django 3.2.6 on 2022-03-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20220208_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, default='DeFault_Name', max_length=45),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(blank=True, default='Tool_DeFault', max_length=45),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(blank=True, default='Bodega_DeFault', max_length=45),
        ),
    ]
