# Generated by Django 3.1.4 on 2021-07-28 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='create_at',
        ),
        migrations.AddField(
            model_name='produto',
            name='criado_em',
            field=models.DateField(auto_created=django.utils.timezone.now, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(max_length=500),
        ),
    ]
