# Generated by Django 5.0.4 on 2024-07-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0014_alter_thumb_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumb',
            name='categoria',
            field=models.CharField(choices=[('SIMULACAO', 'Simulacaoo'), ('ROUGUELIKE', 'Rougue Like'), ('SOBREVIVENCIA', 'Sobrevivencia'), ('EXPLORACAO', 'Exploracao')], default='', max_length=100),
        ),
    ]
