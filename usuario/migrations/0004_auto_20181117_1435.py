# Generated by Django 2.1.3 on 2018-11-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20181117_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='domicilio',
            field=models.TextField(max_length=50),
        ),
    ]