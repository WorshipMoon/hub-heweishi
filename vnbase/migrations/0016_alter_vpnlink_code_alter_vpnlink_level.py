# Generated by Django 5.0.6 on 2024-12-04 12:36

import vnbase.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0015_alter_vpnzfborder_ct_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vpnlink",
            name="code",
            field=models.CharField(
                default=vnbase.models.VpnLink.generate_code, max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="vpnlink",
            name="level",
            field=models.IntegerField(default=1),
        ),
    ]