# Generated by Django 2.2.17 on 2020-12-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='Teste', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]