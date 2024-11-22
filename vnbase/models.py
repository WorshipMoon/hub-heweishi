from django.db import models


# Create your models here.
class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VpnLink(TimeStampedMixin):
    link = models.URLField()
    note = models.TextField()
    code = models.CharField(max_length=50, unique=True)
    status = models.SmallIntegerField(
        default=1,
        choices=[(0, "禁用"), (1, "启用")],
        help_text="状态",
    )
    expiration_time = models.DateTimeField()
    level = models.IntegerField()

    def __str__(self):
        # return f"{self.note} - {self.expiration_time}"
        return self.note


class VpnZfbOrder(TimeStampedMixin):
    price_id = models.IntegerField(help_text="对应的价格Id")
    note = models.CharField(max_length=255, null=True, blank=True, help_text="备注")
    link = models.CharField(max_length=255)
    month = models.IntegerField(help_text="多少个月")
    device = models.IntegerField(help_text="设备数量做记录")
    code = models.CharField(max_length=255, help_text="每个人的码", unique=True)
    status = models.SmallIntegerField(
        default=0,
        choices=[(0, "未激活"), (1, "激活"), (2, "已过期")],
        help_text="状态",
    )
    expiration_time = models.DateTimeField(
        null=True, blank=True, help_text="到期时间(激活的时候写入)"
    )
    pay = models.IntegerField(help_text="需要支付的费用")
    level = models.IntegerField()
    pay_code = models.CharField(max_length=255, help_text="红包口令")
    email = models.CharField(max_length=255)
    pay_status = models.SmallIntegerField(
        default=0,
        choices=[(0, "未结"), (1, "已结")],
        help_text="代理的单是否结算",
    )
    ct_code = models.CharField(max_length=255, null=True, blank=True)
    ct_status = models.IntegerField()

    def __str__(self):
        return self.link


class VpnZfbPrice(TimeStampedMixin):
    note = models.CharField(max_length=255, null=True, blank=True, help_text="备注")
    name = models.CharField(max_length=255, null=True, blank=True, help_text="商品名称")
    month = models.SmallIntegerField(null=True, blank=True, help_text="月份")
    link = models.CharField(max_length=255, null=True, blank=True, help_text="链接")
    code = models.CharField(
        max_length=255, null=True, blank=True, unique=True, help_text="code"
    )
    device = models.SmallIntegerField(null=True, blank=True, help_text="设备数量")
    price = models.IntegerField(help_text="金额")
    status = models.SmallIntegerField(
        default=1,
        choices=[(0, "禁用"), (1, "启用")],
        help_text="状态",
    )
    expiration_time = models.DateTimeField(null=True, blank=True, help_text="到期时间")
    level = models.SmallIntegerField(
        default=1,
        help_text="用户等级\r\n不同的用户等级用不同的节点配置\r\n1用最好的\r\n2一般的\r\n3最一般的",
    )

    # class Meta:
    #     db_table = "vpn_zfb_price"  # 自定义表名无视应用名
    #     verbose_name = "vpn_zfb_price"
    #     verbose_name_plural = "vpn_zfb_price"

    def __str__(self):
        return self.name
