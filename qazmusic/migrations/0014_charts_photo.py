# Generated by Django 4.0.3 on 2022-05-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qazmusic', '0013_genres_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='charts',
            name='photo',
            field=models.ImageField(default=True, upload_to='charts/'),
            preserve_default=False,
        ),
    ]
