# Generated by Django 4.0.1 on 2022-02-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h_w_list', '0004_alter_h_w_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h_w',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Число на которое задано:'),
        ),
    ]
