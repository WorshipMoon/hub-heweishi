# Generated by Django 5.0.6 on 2024-11-22 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0009_alter_vpnzfborder_pay_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vpnzfborder",
            old_name="ctCode",
            new_name="ct_code",
        ),
        migrations.RenameField(
            model_name="vpnzfborder",
            old_name="ctStatus",
            new_name="ct_status",
        ),
    ]