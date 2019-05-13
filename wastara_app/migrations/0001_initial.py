# Generated by Django 2.1 on 2019-05-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('event_time_start', models.CharField(max_length=10)),
                ('event_time_finish', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('body', models.TextField()),
                ('sponsor', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Event Data',
            },
        ),
    ]
