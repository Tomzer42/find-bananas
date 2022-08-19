# Generated by Django 3.0.1 on 2022-08-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bananas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('nb_bananas_1', models.IntegerField()),
                ('nb_bananas_2', models.IntegerField()),
                ('nb_bananas_3', models.IntegerField()),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(upload_to='')),
                ('image_3', models.ImageField(upload_to='')),
            ],
        ),
    ]
