# Generated by Django 5.0.6 on 2024-11-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0013_remove_vpnzfbprice_status_alter_vpnzfbprice_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vpnzfbprice",
            name="status",
            field=models.SmallIntegerField(
                choices=[(0, "禁用"), (1, "启用")], default=1, help_text="状态"
            ),
        ),
    ]