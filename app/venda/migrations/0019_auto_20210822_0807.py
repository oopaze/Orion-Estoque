# Generated by Django 3.1.4 on 2021-08-22 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20210820_0158'),
        ('venda', '0018_auto_20210822_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendaproduto',
            name='produto_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto'),
        ),
    ]
