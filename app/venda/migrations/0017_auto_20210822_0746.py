# Generated by Django 3.1.4 on 2021-08-22 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0016_auto_20210822_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendaproduto',
            old_name='produto',
            new_name='produto_fk',
        ),
        migrations.RenameField(
            model_name='vendaproduto',
            old_name='venda',
            new_name='venda_fk',
        ),
    ]
