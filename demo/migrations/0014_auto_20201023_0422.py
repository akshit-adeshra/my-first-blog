# Generated by Django 2.2.16 on 2020-10-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0013_post_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('GOT', 'GOT'), ('Suits', 'Suits'), ('Dark', 'Dark'), ('Breaking Bad', 'Breaking Bad'), ('Money Heist', 'Money Heist')], default='Null', max_length=20),
        ),
    ]
