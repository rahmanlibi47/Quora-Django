# Generated by Django 4.2.5 on 2023-10-31 11:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qna', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
