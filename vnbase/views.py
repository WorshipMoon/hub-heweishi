from django.shortcuts import render
from django.http import HttpResponse
from .models import VpnLink, VpnZfbOrder, VpnZfbPrice
import os



# Create your views here.
def index(request):
    return HttpResponse("vnbase")


def test(request):
    return HttpResponse("Hello, You're at the TEST. server")


def mvn(request, param):
    print(f"Received request for param: {param}")
    print(f"Request path: {request.path}")
    # 根据请求参数字符串去VpnLink的code对比,并且status=1，返回对应的link
    # 从数据库中获取对应的VpnLink对象
    # print(f"Template path: {os.path.join(settings.BASE_DIR, 'project', 'templates', 'project')}")
    # return HttpResponse("Hello, You're at the HOME. server")
    vpn_link = VpnLink.objects.filter(code=param, status=1).first()
    if vpn_link:
        # 构建响应数据
        response_data = {
            "link": vpn_link.link,
            "expiration_time": vpn_link.expiration_time,
        }
        name = vpn_link.expiration_time.strftime("%Y-%m-%d")
        date_name_daoqi = f"{name}到期"
        date_name2_vx = "VX moonqwe222"
        # 通过level判断返回哪一个模版,把lerver写到模版名称里，类似box{level}.html
        context = {
            "date_name_daoqi": date_name_daoqi,
            "date_name2_vx": date_name2_vx,
            "VN_PASS": os.getenv("VN_PASS"),
        }
        return render(request, f"vnbase/box{vpn_link.level}.html", context)

        # return JsonResponse(response_data)
    else:
        return render(request, "vnbase/error.html")


def zfbvn(request, param):
    print(f"Received request for param: {param}")
    print(f"Request path: {request.path}")
    # 从数据库中获取对应的VpnLink对象
    vpn_link = VpnZfbOrder.objects.filter(code=param, pay_status=1).first()
    if vpn_link:
        if vpn_link.status == 1 or vpn_link.status == 0:
            if vpn_link.status == 0:
                # 表示未激活，这个时候设置status=1，并且写入过期时间
                # 写入过期时间
                from dateutil.relativedelta import relativedelta

                expiration_time = vpn_link.created_at + relativedelta(months=vpn_link.month)
                # 更新过期时间
                vpn_link.expiration_time = expiration_time
                # 更新状态
                vpn_link.status = 1
                vpn_link.save()

            date_name_daoqi = vpn_link.expiration_time.strftime("%Y-%m-%d")
            date_name2_vx = "VX moonqwe222"
            # 通过level判断返回哪一个模版,把lerver写到模版名称里，类似box{level}.html
            context = {
                "date_name_daoqi": date_name_daoqi,
                "date_name2_vx": date_name2_vx,
                "VN_PASS": os.getenv("VN_PASS"),
            }
            return render(request, f"vnbase/box{vpn_link.level}.html", context)
        return render(request, "vnbase/error.html")
    else:
        return render(request, "vnbase/error.html")



