import json
import PyQt5.Qt as qt

modules = dict()

for module in dir(qt):

    try:
        package = getattr(qt, module).__module__
    except AttributeError:
        package = ''

    if package.startswith('PyQt5'):
        modules[module] = package

with open('qt_modules.json', 'w') as file:
    json.dump(modules, file, indent=4)
