# Generated by Django 3.2.6 on 2021-09-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colourMix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColourCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_id', models.CharField(max_length=15)),
                ('base_type', models.CharField(max_length=24)),
                ('colour1', models.CharField(max_length=3)),
                ('colour2', models.CharField(max_length=3)),
                ('colour3', models.CharField(max_length=3)),
                ('colour4', models.CharField(max_length=3)),
                ('colour1_grams', models.FloatField()),
                ('colour2_grams', models.FloatField()),
                ('colour3_grams', models.FloatField()),
                ('colour4_grams', models.FloatField()),
            ],
        ),
    ]
