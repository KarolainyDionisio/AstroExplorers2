# Generated by Django 5.1.1 on 2024-12-10 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_perfil_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='imagem_perfil',
        ),
    ]