# Generated by Django 3.2.7 on 2021-09-19 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_usuario_pis'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usuario',
            unique_together={('nome', 'email'), ('nome', 'cpf'), ('nome', 'pis')},
        ),
    ]
