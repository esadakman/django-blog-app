# Generated by Django 4.1.1 on 2022-09-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_post_blog_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(default=""),
        ),
    ]
