# Generated by Django 3.1.4 on 2021-08-22 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0013_auto_20210822_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produtos_fk',
        ),
    ]