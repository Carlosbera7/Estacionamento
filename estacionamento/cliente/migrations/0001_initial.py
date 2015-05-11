# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('endereco', models.CharField(max_length=100, null=True, verbose_name=b'Endere\xc3\xa7o')),
                ('Carro', models.ForeignKey(verbose_name=b'Carro', to='carro.Carro', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
