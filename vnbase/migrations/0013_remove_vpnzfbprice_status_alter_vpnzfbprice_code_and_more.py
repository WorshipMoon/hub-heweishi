# Generated by Django 5.0.6 on 2024-11-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0012_alter_vpnzfbprice_level"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vpnzfbprice",
            name="status",
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="code",
            field=models.CharField(
                blank=True, help_text="code", max_length=255, null=True, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="device",
            field=models.SmallIntegerField(blank=True, help_text="设备数量", null=True),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="expiration_time",
            field=models.DateTimeField(blank=True, help_text="到期时间", null=True),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="link",
            field=models.CharField(
                blank=True, help_text="链接", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="month",
            field=models.SmallIntegerField(blank=True, help_text="月份", null=True),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="name",
            field=models.CharField(
                blank=True, help_text="商品名称", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="note",
            field=models.CharField(
                blank=True, help_text="备注", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="price",
            field=models.IntegerField(help_text="金额"),
        ),
    ]