# Generated by Django 4.1.7 on 2023-03-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_post_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]