# Generated by Django 3.1.4 on 2021-08-22 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0014_remove_venda_produtos_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendaproduto',
            name='venda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='venda.venda'),
        ),
    ]