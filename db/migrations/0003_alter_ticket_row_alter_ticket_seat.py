# Generated by Django 4.0.2 on 2023-06-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0002_user_order_alter_movie_title_ticket_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="row",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="seat",
            field=models.IntegerField(),
        ),
    ]
