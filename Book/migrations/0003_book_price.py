# Generated by Django 4.1.3 on 2022-12-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
