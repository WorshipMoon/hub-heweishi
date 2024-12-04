from django.db import models
import uuid


# Create your models here.
class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VpnLink(TimeStampedMixin):
    def generate_code():
        return str(uuid.uuid4())

    link = models.URLField(null=True, blank=True)
    note = models.TextField()
    code = models.CharField(max_length=50, unique=True, default=generate_code, help_text="每个链接的码")
    status = models.SmallIntegerField(
        default=1,
        choices=[(0, "禁用"), (1, "启用")],
        help_text="状态",
    )
    expiration_time = models.DateTimeField()
    level = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.link and self.code:  # 如果 link 没有被设置，并且 code 已存在
            # https://cc.vape755.com/mvn/b0230bcf-3b47-4751-bb2e-c0526860478e
            self.link = f"https://cc.vape755.com/mvn/{self.code}"
        super().save(*args, **kwargs)  # 调用父类的 save 方法保存实例

    def __str__(self):
        # return f"{self.note} - {self.expiration_time}"
        return self.note


class VpnZfbOrder(TimeStampedMixin):
    price_id = models.IntegerField(help_text="对应的价格Id")
    note = models.CharField(max_length=255, null=True, blank=True, help_text="备注")
    link = models.CharField(max_length=255)
    month = models.IntegerField(help_text="多少个月")
    device = models.IntegerField(help_text="设备数量做记录")
    code = models.CharField(max_length=50, help_text="每个链接的码", unique=True)
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
        choices=[(0, "未收款"), (1, "已收")],
        help_text="收款状态",
    )
    ct_code = models.CharField(max_length=255, null=True, blank=True)
    ct_status = models.SmallIntegerField(
        default=0, help_text="代理的单是否结算 1已结 0 未结"
    )

    def __str__(self):
        return self.email


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
