# Generated by Django 5.1.3 on 2024-11-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.TextField()),
                ('name', models.TextField()),
                ('dis', models.TextField()),
                ('price', models.IntegerField()),
                ('offer_price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
