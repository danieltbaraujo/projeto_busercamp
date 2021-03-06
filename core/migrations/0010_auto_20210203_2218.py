# Generated by Django 3.1.5 on 2021-02-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_fatura_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacao',
            name='mes_final',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='operacao',
            name='estabelecimento',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='operacao',
            name='prestacoes_total',
            field=models.IntegerField(blank=True),
        ),
    ]
