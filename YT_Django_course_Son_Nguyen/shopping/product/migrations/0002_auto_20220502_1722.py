# Generated by Django 2.2 on 2022-05-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
