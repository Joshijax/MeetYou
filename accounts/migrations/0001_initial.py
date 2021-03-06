# Generated by Django 3.0.5 on 2020-04-21 21:36

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
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('whatapp_number', models.CharField(max_length=100)),
                ('Business_Name', models.CharField(max_length=100)),
                ('Employment_status', models.CharField(max_length=100)),
                ('Facebook_link', models.CharField(max_length=100)),
                ('Successfully_trans', models.IntegerField(default=0)),
                ('role', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='gallery/profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
