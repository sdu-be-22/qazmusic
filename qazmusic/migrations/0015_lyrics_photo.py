# Generated by Django 4.0.3 on 2022-05-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qazmusic', '0014_charts_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='photo',
            field=models.ImageField(default=True, upload_to='lyrics/'),
            preserve_default=False,
        ),
    ]