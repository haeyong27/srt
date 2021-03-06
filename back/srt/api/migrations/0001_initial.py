# Generated by Django 2.2.9 on 2020-01-25 12:42

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
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srtid', models.CharField(max_length=30)),
                ('srtpw', models.CharField(max_length=30)),
                ('logintype', models.CharField(max_length=30)),
                ('dpt', models.CharField(max_length=30)),
                ('arr', models.CharField(max_length=30)),
                ('adult', models.CharField(max_length=30)),
                ('child', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('dptime', models.CharField(max_length=30)),
                ('ticketnum', models.CharField(max_length=30)),
                ('is_complete', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
