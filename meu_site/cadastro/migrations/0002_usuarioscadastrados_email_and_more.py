# Generated by Django 5.1.4 on 2025-01-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioscadastrados',
            name='email',
            field=models.EmailField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='usuarioscadastrados',
            name='nome_completo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
