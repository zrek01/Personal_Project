# Generated by Django 3.0.8 on 2020-07-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='portfolio/images/')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
