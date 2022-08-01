from plugins.lib.springboot.main import springboot_scan
from plugins.plugin import Plugin


class RTPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.type = 3
        self.name = "springboot_rce"
        self.desc = "springboot actuator未授权访问中某些组件会导致rce，该插件会扫描所有组件，依次进行poc验证"

    def run(self):
        self._run()

    def _run(self):
        self.log(f"scan {self.url}")
        self.log(springboot_scan(self.url, self.vps))

