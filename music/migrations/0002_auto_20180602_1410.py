# Generated by Django 2.0.5 on 2018-06-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.CharField(default='', max_length=200),
        ),
    ]
