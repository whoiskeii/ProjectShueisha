# Generated by Django 4.1.1 on 2022-09-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_skill_userprofile"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "ordering": ["timestamp"],
                "verbose_name": "Shueisha Blog",
                "verbose_name_plural": "Shueisha Blogs",
            },
        ),
        migrations.AlterModelOptions(
            name="contactprofile",
            options={
                "ordering": ["timestamp"],
                "verbose_name": "User Blog",
                "verbose_name_plural": "User Blogs",
            },
        ),
    ]