from uuid import uuid4
from django.utils import timezone

from vnbase.mail import send_order_email
from .models import VpnLink, VpnZfbOrder, VpnZfbPrice
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import transaction

#  'api/zfbwebvn/ZfbVnPriceList',


@csrf_exempt
def ZfbVnPriceList(request):
    if request.method == "POST":
        # 获取VpnZfbPrice表中status为1的数据，并以price字段升序排序
        price_list = VpnZfbPrice.objects.filter(status=1).order_by("price")
        # 将数据转换为列表
        price_data = list(price_list.values())
        # 将数据转换为JSON格式
        response_data = {
            "status": 1,
            "res": price_data,
        }
        # 返回JSON数据
        return JsonResponse(response_data)


@csrf_exempt
@transaction.atomic
def ZfbVnOrderCreate(request):
    if request.method == "POST":
        try:
            # 处理有效数据
            data = json.loads(request.body)
            price_id = data.get("price_id")
            email = data.get("email")
            pay_code = data.get("pay_code")
            # 判断price_id是否存在于VpnZfbPrice表中
            priceRes = VpnZfbPrice.objects.filter(id=price_id).first()
            if not priceRes:
                # 如果不存在，则返回错误信息
                return JsonResponse(
                    {
                        "status": 0,
                        "message": "price_id不存在",
                    }
                )

            # 判断是否已经存在pay_code，pay_status为0的记录
            existing_order = VpnZfbOrder.objects.filter(
                pay_code=pay_code, pay_status=0
            ).first()
            if existing_order:
                # 如果存在，则返回错误信息
                return JsonResponse(
                    {
                        "status": 2,
                        "message": "口令重复, 请勿重复提交",
                    }
                )
            # 进行业务逻辑处理
            # 写入新的订单，生成订单数据
            code = uuid4()
            data = {
                "code": code,
                "link": f"https://cc.vape755.com/zfbvn/{code}",
                "price_id": price_id,
                "email": email,
                "pay_code": pay_code,
                "status": 0,
                "month": priceRes.month,
                "device": priceRes.device,
                "pay": priceRes.price,
                "level": priceRes.level,
            }

            # 写入新的订单
            order = VpnZfbOrder.objects.create(**data)
            # 读取 HTML 文件内容
            # template_path = os.path.join(os.path.dirname(__file__), 'email_template.html')
            # with open(template_path, 'r', encoding='utf-8') as file:
            # html_message = file.read()
            activation_link = f"https://bvn.vape755.com/api/zfbwebvn/ZfbVnOrderLinkSetPay?id={order.id}&act=1&type=1"
            html_message = f"""
                                <html>
                                    <body>
                                        <h1>{ priceRes.name }</h1>
                                        <h1>{ email }</h1>
                                        <h1>{ priceRes.price }</h1>
                                        <h1>{ pay_code }</h1>
                                        <p><a href="{ activation_link }" target="_blank" rel="noopener noreferrer">处理发</a></p>
                                    </body>
                                </html>
                            """
            send_order_email("新节点订单", "123", ["736555030@qq.com"], html_message)
            print(price_id, email, pay_code)
            return JsonResponse(
                {
                    "status": 1,
                    "message": "成功",
                    "res": {
                        "id": order.id,
                        "email": order.email,
                        "pay_code": order.pay_code,
                    },
                }
            )
        except Exception as e:
            # 回滚事务
            transaction.set_rollback(True)
            return JsonResponse({"status": -1, "message": str(e)}, status=500)


@csrf_exempt
@transaction.atomic
def ZfbVnOrderLinkSetPay(request):
    if request.method == "GET":
        id = request.GET.get("id")
        act = request.GET.get("act")
        type = request.GET.get("type")
        if act == "1":
            if type == "1":
                order = VpnZfbOrder.objects.filter(id=id).first()
                if order:
                    if order.pay_status == 1:
                        return HttpResponse("已经处理过了")

                    order.pay_status = 1
                    order.save()
                    html_message = f"""
                                        <html>
                                            <body>
                                                <div>下单时间: { order.created_at }</div>
                                                <p>节点链接(复制去导入, 不会可以看说明, 说明在购买的页面):</p>
                                                <p>{ order.link }</p>
                                            </body>
                                        </html>
                                    """
                    send_order_email("节点订单", "123", [order.email], html_message)
                    return HttpResponse("ok")


@csrf_exempt
def ZfbVnOrderLinkGet(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        # 查找这个email的所有订单
        orders = VpnZfbOrder.objects.filter(email=email, pay_status=1)
        # 如果orders > 0 则遍历并组装html用于发送邮件
        if orders.count() > 0:
            html_message = "<html><body>"
            for order in orders:
                html_message += f"""
                                    <div>下单时间: { order.created_at }</div>
                                    <p>链接(用于导入, 不会可以看说明):{ order.link }</p>
                                """
            html_message += "</body></html>"
            send_order_email("节点订单", "123", [email], html_message)
            return JsonResponse({"status": 1, "message": "已发送到邮箱"})


@csrf_exempt
def ZfbVnOrderLinkFirst(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order_id = data.get("order_id")
        email = data.get("email")
        pay_code = data.get("pay_code")
        type = data.get("type")
        # print(order_id)
        if type == 1:
            order = VpnZfbOrder.objects.filter(
                id=order_id, email=email, pay_code=pay_code, pay_status=1
            ).first()
            if order:
                return JsonResponse(
                    {"status": 1, "message": "处理成功", "link": order.link}
                )
        return JsonResponse({"status": 2})
