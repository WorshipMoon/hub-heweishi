# Generated by Django 5.0.6 on 2024-11-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VpnLinks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("link", models.URLField()),
                ("note", models.TextField()),
                ("code", models.CharField(max_length=50)),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "0禁用"), (1, "启用")], default=2, help_text="状态"
                    ),
                ),
                ("expiration_time", models.DateTimeField()),
                ("level", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
