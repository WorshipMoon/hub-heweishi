from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("vnbase")


def test(request):
    return HttpResponse("Hello, You're at the TEST. server")
