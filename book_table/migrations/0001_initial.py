# Generated by Django 5.0.4 on 2024-04-20 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_people', models.IntegerField()),
                ('book_tables', models.IntegerField()),
                ('book_note', models.CharField(max_length=255)),
                ('book_name', models.CharField(max_length=255)),
                ('book_phone', models.CharField(max_length=255)),
                ('book_when', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
