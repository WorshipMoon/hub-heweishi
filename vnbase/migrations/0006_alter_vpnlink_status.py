# Generated by Django 5.0.6 on 2024-11-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0005_delete_vpnlinks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vpnlink",
            name="status",
            field=models.SmallIntegerField(
                choices=[(0, "禁用"), (1, "启用")], default=2, help_text="状态"
            ),
        ),
    ]
