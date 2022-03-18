# Generated by Django 4.0.3 on 2022-03-18 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ournft_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Text')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('image', models.ImageField(upload_to=ournft_app.models.image_path, verbose_name='Image')),
                ('image_hash', models.CharField(max_length=64, null=True)),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Text')),
                ('visibility', models.BooleanField(verbose_name='Visible')),
                ('secret', models.CharField(max_length=50, verbose_name='Secret')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
