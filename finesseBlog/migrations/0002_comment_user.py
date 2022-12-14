# Generated by Django 3.2.15 on 2022-10-13 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Comments migrations for comments section"""
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finesseBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey
            (blank=True, null=True,
             on_delete=django.db.models.deletion.CASCADE,
             related_name='comments',
             to=settings.AUTH_USER_MODEL),
        ),
    ]
