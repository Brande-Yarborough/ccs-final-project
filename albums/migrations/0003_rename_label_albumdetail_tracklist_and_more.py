# Generated by Django 4.1.7 on 2023-03-12 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_remove_albumdetail_release_title_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumdetail',
            old_name='label',
            new_name='tracklist',
        ),
        migrations.RemoveField(
            model_name='albumdetail',
            name='track',
        ),
    ]
