# Generated by Django 3.0.8 on 2020-07-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20200706_1056'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cover',
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(default='', upload_to='portfolio/images/'),
        ),
    ]
