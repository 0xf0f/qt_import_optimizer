import json
from PyQt5.QtCore import Qt as constants

_imported_modules = {
    'constants': constants
}

with open('qt_modules.json') as file:
    module_packages = json.load(file)


def __getattr__(name):
    try:
        module = _imported_modules[name]
    except KeyError:
        module = getattr(
            __import__(module_packages[name], fromlist=[name]),
            name
        )
        _imported_modules[name] = module

    return module