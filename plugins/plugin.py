import traceback


class Plugin(object):

    def __init__(self):
        self.URL_CMD = 1
        self.CMD = 2
        self.URL_SHELL = 3
        self.name = None
        '''
        插件类型，为URL,CMD两种类型，前端显示不同
        '''
        self.type = None
        self.url = None
        self.host = None
        self.port = None
        self.cmd = None
        self.result = ''
        self.desc = None
        self.vps = None

    def run(self):
        try:
            self._run()
        except Exception as e:
            self.log(traceback.format_exc())

    def _run(self):
        raise NotImplementedError

    def log(self, content):
        if content is None:
            return
        self.result += "[+] " + content + "\n"
