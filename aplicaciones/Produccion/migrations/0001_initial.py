# Generated by Django 4.2.7 on 2023-11-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('codigo', models.CharField(max_length=30)),
                ('descuento', models.PositiveSmallIntegerField()),
                ('precio', models.PositiveSmallIntegerField()),
            ],
        ),
    ]