# Generated by Django 5.1.7 on 2025-03-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Home Stay', 'Home Stay'), ('Canal Boating', 'Canal Boating'), ('kayaking', 'kayaking'), ('Shikkara', 'Shikkara')], default='Home Stay', max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('choose_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='service images')),
            ],
        ),
    ]
