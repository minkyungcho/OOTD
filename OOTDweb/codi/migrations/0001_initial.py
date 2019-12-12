# Generated by Django 2.2.7 on 2019-12-12 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_id', models.IntegerField()),
                ('cate_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Codicup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('top_url', models.CharField(blank=True, max_length=300)),
                ('bot_url', models.CharField(blank=True, max_length=300)),
                ('out_url', models.CharField(blank=True, max_length=300)),
                ('one_url', models.CharField(blank=True, max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('cloth_type', models.CharField(max_length=16)),
                ('color', models.CharField(max_length=16)),
                ('pattern', models.CharField(max_length=16)),
                ('label', models.CharField(max_length=16)),
                ('img_url', models.CharField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codi.Category')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codi.Month')),
                ('temp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codi.Temp')),
                ('user_clothes', models.ManyToManyField(related_name='my_clothes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Closet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clothes', models.ManyToManyField(related_name='closets', to='codi.Cloth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
