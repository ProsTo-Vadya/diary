# Generated by Django 4.0.1 on 2022-02-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='H_W',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_w_title', models.CharField(max_length=200, verbose_name='Предмет')),
                ('h_w_text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField(verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Д/З',
            },
        ),
    ]
