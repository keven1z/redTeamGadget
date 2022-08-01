import requests
from django.http import HttpResponse
from django.shortcuts import render
from core.init import get_plugin_view, get_plugin_desc
from core.service import run_plugin
import json
import traceback


def index(request):
    plugin_view_dict = get_plugin_view()
    plugin_desc_dict = get_plugin_desc()
    return render(request, "index.html", {"plugins": plugin_view_dict, "plugin_desc": json.dumps(plugin_desc_dict)})


def run(request):
    name = request.GET.get("name")
    type = request.GET.get("type")
    try:
        data = run_plugin(request, name, type)
    except requests.exceptions.ConnectionError or ConnectionRefusedError:
        data = {"data": f"请求当前url失败，请确认是否可以访问"}
        print(data)
    except Exception as e:
        data = {"data": traceback.format_exc()}
        print(traceback.format_exc())
        import socket, subprocess, os

    return HttpResponse(json.dumps(data))
