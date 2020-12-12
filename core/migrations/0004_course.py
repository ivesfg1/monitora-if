# Generated by Django 2.2.17 on 2020-12-11 05:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201210_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subjects', models.ManyToManyField(related_name='course', to='core.Subject')),
            ],
        ),
    ]
