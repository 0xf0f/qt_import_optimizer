import re
import json

from pathlib import Path
from sortedcontainers import SortedSet

import PyQt5.Qt as qt

qt_regex = re.compile(r'qt\.([a-zA-Z_][a-zA-Z_0-9]*)', re.IGNORECASE)
file_path = Path(__file__)

exclude = [
    '.idea',
    '.venv',
    'qt.py',
    'qt_all.py'
    'qt_import_optimizer.py'
]

imports = SortedSet()

stack = [file_path.parents[0].iterdir()]
while stack:
    iterator = stack[-1]

    try:
        item = next(iterator)
    except StopIteration:
        stack.pop()
        continue

    path = Path(item)
    if path.name in exclude:
        continue

    if path.suffix == '.py':
        with open(path) as file:
            for line in file:
                for class_name in qt_regex.findall(line):
                    if class_name in ('py', 'constants'):
                        continue
                    class_object = getattr(qt, class_name)
                    import_info = class_name, class_object.__module__
                    imports.add(import_info)

with open('qt.py', 'w') as file:
    for module, package in imports:
        print('from', package, 'import', module, file=file)

    print(file=file)
    print('from PyQt5.QtCore import Qt as constants', file=file)
