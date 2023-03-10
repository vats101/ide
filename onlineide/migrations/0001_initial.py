# Generated by Django 4.1.4 on 2022-12-20 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=2000)),
                ('language', models.CharField(max_length=50)),
                ('submission_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('S', 'Success'), ('E', 'Error'), ('P', 'Pending')], max_length=1)),
                ('user_input', models.CharField(blank=True, max_length=200, null=True)),
                ('output', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineide.user')),
            ],
        ),
    ]
