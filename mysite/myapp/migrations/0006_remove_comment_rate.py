# Generated by Django 4.2.2 on 2023-07-09 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_comment_rate"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="rate",),
    ]
