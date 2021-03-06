# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-30 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('deuda', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=300)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Producto')),
            ],
        ),
    ]
