# Generated by Django 4.0.3 on 2022-04-17 07:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message='The format should be exactly be of 10 digits', regex='^\\+?1?\\d{10}$')])),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='webUser',
            fields=[
                ('webUserid', models.AutoField(primary_key=True, serialize=False)),
                ('Susername', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='home/images')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('usertype', models.CharField(choices=[('webUser', 'webUser'), ('User', 'User')], max_length=20, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
