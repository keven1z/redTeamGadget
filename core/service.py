from core.init import get_plugin_hash


def run_plugin(request, name, type):
    try:
        plugin = get_plugin_hash()[name].module_obj
    except KeyError:
        return {
            "data": f"没有找到对应的插件:{name}"
        }
    if type == "2":
        ip = request.GET.get("ip")
        port = request.GET.get("port")
        cmd = request.GET.get("cmd")
        plugin.cmd = cmd
        plugin.host = ip
        plugin.port = int(port)
        plugin.run()
    elif type == "3":
        url = request.GET.get("url")
        plugin.url = url
        plugin.vps = request.GET.get("vps")
        plugin.run()
    elif type == "1":
        url = request.GET.get("url")
        plugin.url = url
        plugin.cmd = request.GET.get("cmd")
        plugin.run()
    else:
        return {
            "data": f"没有找到对应的插件类型:{type}"
        }
    data = {
        "data": plugin.result
    }
    return data
