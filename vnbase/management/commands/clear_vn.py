from django.core.management.base import BaseCommand
from vnbase.models import VpnLink, VpnZfbOrder
from django.utils import timezone
from vnbase.mail import send_order_email

class Command(BaseCommand):
    help = 'This command does clear vn'

    # def add_arguments(self, parser):
    #     # 添加命令行参数（可选）
    #     parser.add_argument('--name', type=str, help='Name of the person')

    def handle(self, *args, **options):
        # 获取vpnlink过期的订单 expiration_time < 现在时间 并且status=1的订单
        expired_orders = VpnLink.objects.filter(expiration_time__lt=timezone.now(), status=1)
        print("expired_orders的数量:", expired_orders.count())
        if expired_orders.count() > 0:
            for order in expired_orders:
                order.status = 0
                order.save()
            html_message = f"""
                                <html>
                                    <body>
                                        <p>有{expired_orders.count()}条默认节点已经过期, 请尽快处理</p>
                                    </body>
                                </html>
                            """
            send_order_email("vn过期提醒", "123", ["736555030@qq.com"], html_message)
                

        # 获取vpnzfborder过期的订单 expiration_time < 现在时间 并且status=1的订单
        expired_orders = VpnZfbOrder.objects.filter(expiration_time__lt=timezone.now(), status=1)
        print("zfbvnexpired_orders的数量:", expired_orders.count())
        if expired_orders.count() > 0:
            for order in expired_orders:
                order.status = 2
                order.save()
            # html_message = f"""
            #                     <html>
            #                         <body>
            #                             <p>有{expired_orders.count()}条zfbvn节点已经过期, 请尽快处理</p>
            #                         </body>
            #                     </html>
            #                 """
            # send_order_email("vn过期提醒", "123", ["736555030@qq.com"], html_message)
        self.stdout.write(self.style.SUCCESS("Successfully cleared vn"))