# Generated by Django 4.1.1 on 2022-09-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_remove_userprofile_cv"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactprofile",
            name="title",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Title"
            ),
        ),
    ]
