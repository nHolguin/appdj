# Generated by Django 2.2.1 on 2019-05-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('posicion', models.CharField(max_length=200)),
                ('oficina', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('inicio', models.DateTimeField()),
                ('salario', models.FloatField()),
            ],
        ),
    ]
