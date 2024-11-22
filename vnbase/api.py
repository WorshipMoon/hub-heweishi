from django.utils import timezone
from.models import VpnLink

# # 创建一个字典，包含与VpnLink模型字段相对应的数据
# data = {
#     'link': 'https://cc.vape755.com/mvn/33ac2445-68d1-493e-bfcc-427ea3e2d24d',
#     'note': '测试1微信四季',
#     'code': '33ac2445-68d1-493e-bfcc-427ea3e2d24d',
#     'status': True,
#     'expiration_time': timezone.datetime(2024, 2, 26, 4, 34, 28),
#     'level': 1,
#     'created_at': timezone.datetime(2024, 2, 4, 17, 30, 27),
#     'updated_at': timezone.datetime(2024, 2, 26, 4, 35, 3)
# }

# # 创建一个新的VpnLink对象，并将字典中的数据分配给它的字段
# new_link = VpnLink(**data)

# # 保存新的VpnLink对象到数据库
# new_link.save()