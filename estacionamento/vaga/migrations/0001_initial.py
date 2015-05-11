# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=15, null=True, verbose_name=b'Valor')),
                ('tempo', models.CharField(max_length=10, null=True, verbose_name=b'Tempo')),
                ('Carro', models.ForeignKey(verbose_name=b'Carro', to='carro.Carro', null=True)),
                ('Cliente', models.ForeignKey(verbose_name=b'Cliente', to='cliente.Cliente', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=10, null=True, verbose_name=b'Numero')),
                ('localizacao', models.CharField(max_length=100, null=True, verbose_name=b'Localiza\xc3\xa7\xc3\xa3o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alugar',
            name='vaga',
            field=models.ForeignKey(verbose_name=b'Vaga', to='vaga.Vaga', null=True),
            preserve_default=True,
        ),
    ]
