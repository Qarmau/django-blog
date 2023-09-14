# Generated by Django 4.2.4 on 2023-09-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('blogtopic', models.CharField(choices=[('World', 'World'), ('Kenya', 'Kenya'), ('Africa', 'Africa'), ('Technology', 'Technology'), ('Design', 'Design'), ('Business', 'Business'), ('Politics', 'Politics'), ('Opinion', 'Opinion'), ('Science', 'Science'), ('Health', 'Health'), ('Style', 'Style'), ('Travel', 'Travel')], max_length=20)),
            ],
        ),
    ]
