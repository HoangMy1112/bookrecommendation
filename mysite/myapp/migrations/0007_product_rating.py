# Generated by Django 4.2.2 on 2023-07-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_remove_comment_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="product", name="rating", field=models.IntegerField(default=0),
        ),
    ]
