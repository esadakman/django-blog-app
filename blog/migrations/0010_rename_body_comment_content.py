# Generated by Django 4.1.1 on 2022-09-11 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="body",
            new_name="content",
        ),
    ]
