# Generated by Django 5.0.6 on 2024-11-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vnbase", "0011_vpnzfbprice_alter_vpnzfborder_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vpnzfbprice",
            name="level",
            field=models.SmallIntegerField(
                default=1,
                help_text="用户等级\r\n不同的用户等级用不同的节点配置\r\n1用最好的\r\n2一般的\r\n3最一般的",
            ),
        ),
    ]
