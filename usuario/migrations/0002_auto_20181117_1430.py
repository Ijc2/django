# Generated by Django 2.1.3 on 2018-11-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=50)),
                ('Localizacion', models.CharField(max_length=50)),
                ('Monto', models.IntegerField()),
                ('Plazo_Ejecucion', models.DateField(max_length=10)),
                ('Detalle_monto', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='domicilio',
            field=models.TextField(max_length=50),
        ),
    ]
