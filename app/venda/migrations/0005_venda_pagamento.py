# Generated by Django 3.1.4 on 2021-08-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0004_auto_20210819_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='pagamento',
            field=models.CharField(choices=[('dinheiro', 'Dinheiro'), ('cartão', 'Cartão')], default='dinheiro', max_length=50, verbose_name='Método de Pagamento'),
            preserve_default=False,
        ),
    ]
