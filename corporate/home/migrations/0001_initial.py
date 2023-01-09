# Generated by Django 3.0 on 2022-04-12 10:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(max_length=11)),
                ('join_date', models.DateField()),
                ('total_fees', models.IntegerField()),
                ('module', models.CharField(choices=[('mern', 'mern'), ('java fullstack', 'java fullstack'), ('python fullstack', 'python fullstack')], max_length=20)),
                ('image', models.ImageField(upload_to='pics')),
                ('status', models.CharField(choices=[('training', 'training'), ('placed', 'placed'), ('complete', 'complete')], max_length=20)),
                ('joining_location', models.CharField(choices=[('bhanwarkua', 'bhanwarkua'), ('vijay_nagar', 'vijay_nagar'), ('ujjain', 'ujjain')], max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.TextField()),
                ('date', models.DateField()),
                ('timings_for_day', models.CharField(max_length=50)),
                ('remarks', models.TextField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student')),
            ],
        ),
    ]
