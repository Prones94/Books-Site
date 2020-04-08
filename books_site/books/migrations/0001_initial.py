# Generated by Django 3.0.4 on 2020-04-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('num_pages', models.IntegerField()),
                ('date_published', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
