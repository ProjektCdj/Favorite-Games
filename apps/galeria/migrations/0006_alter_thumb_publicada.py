# Generated by Django 5.0.4 on 2024-07-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_thumb_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumb',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
