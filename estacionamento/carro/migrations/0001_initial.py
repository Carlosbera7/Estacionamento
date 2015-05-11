# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=50, null=True, verbose_name=b'Modelo')),
                ('cor', models.CharField(max_length=20, null=True, verbose_name=b'Cor')),
                ('marca', models.CharField(max_length=50, null=True, verbose_name=b'Marca')),
                ('placa', models.CharField(max_length=10, null=True, verbose_name=b'Placa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
