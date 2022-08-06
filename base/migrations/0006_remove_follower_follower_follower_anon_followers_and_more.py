# Generated by Django 4.0.3 on 2022-03-20 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_anonymous_user_like_anon_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='follower',
        ),
        migrations.AddField(
            model_name='follower',
            name='anon_followers',
            field=models.ManyToManyField(related_name='anon_followers', to='base.anonymoususer'),
        ),
        migrations.AddField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]