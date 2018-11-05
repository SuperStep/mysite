# Generated by Django 2.1.2 on 2018-11-03 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256)),
                ('mainImage', models.ImageField(blank=True, upload_to='images/places/main')),
                ('image1', models.ImageField(blank=True, upload_to='images/places/')),
                ('image2', models.ImageField(blank=True, upload_to='images/places/')),
                ('image3', models.ImageField(blank=True, upload_to='images/places/')),
                ('description', models.TextField(max_length=3000)),
                ('coord_lon', models.FloatField()),
                ('coord_lat', models.FloatField()),
                ('site_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='place',
            index_together={('id', 'slug')},
        ),
    ]
