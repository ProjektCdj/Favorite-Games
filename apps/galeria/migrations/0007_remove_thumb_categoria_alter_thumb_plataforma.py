# Generated by Django 5.0.4 on 2024-07-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_alter_thumb_publicada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumb',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='thumb',
            name='plataforma',
            field=models.BooleanField(choices=[('PC', 'Pc'), ('XBOX', 'Xbox'), ('PLAYSTATION', 'Playstation'), ('SWITCH', 'Switch')], max_length=11),
        ),
    ]
