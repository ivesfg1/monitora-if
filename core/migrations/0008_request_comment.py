# Generated by Django 2.2.17 on 2020-12-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='comment',
            field=models.TextField(default='test', max_length=1000),
            preserve_default=False,
        ),
    ]