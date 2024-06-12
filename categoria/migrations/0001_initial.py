# Generated by Django 5.0.6 on 2024-06-12 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
                ('barra', models.CharField(max_length=20)),
                ('activo', models.IntegerField()),
                ('id_categoria', models.ForeignKey(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria')),
            ],
        ),
    ]
