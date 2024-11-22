from django.http import HttpResponse, JsonResponse
from decouple import config
from django.conf import settings
from pathlib import Path
import logging

# 获取 logger
logger = logging.getLogger(__name__)


def index(request):

    logger.info("This is an info message")
    return HttpResponse("Hello, You're at the HOME. server")


def config_view(request):
    config_dict = {
        k: str(v) if isinstance(v, Path) else v
        for k, v in settings.__dict__.items()
        if k.isupper()
    }
    return JsonResponse(config_dict)


def test(request):
    return HttpResponse("Hello, You're at the TEST. server")


def mvn(request, param):
    print(f"Received request for param: {param}")
    print(f"Request path: {request.path}")
    return HttpResponse(f"mvn {param}")
