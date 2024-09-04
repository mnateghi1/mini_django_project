# Generated by Django 5.1 on 2024-09-03 16:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=205)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=250)),
                ('number_of_pages', models.IntegerField(default=0)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published'), ('RJ', 'Rejected')], default='DR', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
                'indexes': [models.Index(fields=['-published'], name='library_boo_publish_b07fd2_idx')],
            },
        ),
    ]
