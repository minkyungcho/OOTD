# Generated by Django 2.2.7 on 2019-12-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='domColor',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='palColor1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='palColor2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='palColor3',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='palColor4',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
