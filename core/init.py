from plugins.plugin_manager import PluginManager

p = PluginManager()
p.load()


def get_plugin_view() -> dict:
    '''
    获取插件类型
    :return: dict
    '''
    module_view = p.module_view
    return module_view


def get_plugin_desc() -> dict:
    """
    获取所有插件描述
    :rtype: dict
    """
    module_desc = p.module_desc
    return module_desc


def get_plugin_hash() -> dict:
    module_hash = p.module_hash
    return module_hash


if __name__ == '__main__':
    print(get_plugin_hash()['JDWP'].module_obj)
