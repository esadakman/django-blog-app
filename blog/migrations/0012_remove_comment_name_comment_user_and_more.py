# Generated by Django 4.1.1 on 2022-09-12 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0011_alter_post_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="name",
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date_added",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
