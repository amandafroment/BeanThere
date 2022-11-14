# Generated by Django 4.1.1 on 2022-11-11 22:31

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lighting', models.CharField(max_length=50)),
                ('sound', models.CharField(max_length=50)),
                ('airconditioning', models.BooleanField()),
                ('patio', models.BooleanField()),
                ('pet_friendly', models.BooleanField()),
                ('traffic', models.CharField(max_length=50)),
                ('food', models.BooleanField()),
                ('drinks', models.BooleanField()),
                ('wifi', models.BooleanField()),
                ('outlets', models.BooleanField()),
                ('comments', models.TextField(max_length=250)),
                ('cafe_id', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]