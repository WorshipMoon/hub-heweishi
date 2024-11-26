from django.urls import path
from . import views, api


app_name = "vnbase"


urlpatterns = [
    path("", views.index, name="index"),
    # path("mvn/<str:param>", views.mvn, name="mvn"),
    # path("zfbvn/<str:param>", views.zfbvn, name="zfbvn"),
    #  'api/zfbwebvn/ZfbVnPriceList',
    path("zfbwebvn/ZfbVnPriceList", api.ZfbVnPriceList),
    path("zfbwebvn/ZfbVnOrderCreate", api.ZfbVnOrderCreate),
    path("zfbwebvn/ZfbVnOrderLinkSetPay", api.ZfbVnOrderLinkSetPay),
    path("zfbwebvn/ZfbVnOrderLinkGet", api.ZfbVnOrderLinkGet),
    path("zfbwebvn/ZfbVnOrderLinkFirst", api.ZfbVnOrderLinkFirst),
]

