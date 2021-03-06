# Generated by Django 3.1.4 on 2021-08-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20210728_0005'),
        ('venda', '0003_auto_20210805_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produto',
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos_fk',
            field=models.ManyToManyField(to='produto.Produto', verbose_name='Produtos'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
