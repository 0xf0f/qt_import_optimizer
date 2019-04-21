import re
import PyQt5.Qt as qt

from pathlib import Path
from sortedcontainers import SortedSet

qt_regex = re.compile(r'qt\.([a-zA-Z_][a-zA-Z_0-9]*)', re.IGNORECASE)
file_path = Path(__file__)

exclude = [
    '.idea',
    '.venv',
    '.git',
    '__pycache__',
    'qt.py',
    'qt_all.py',
    'qt_auto.py',
    'qt_json_generator.py',
    'qt_import_optimizer.py'
]

imports = SortedSet()

stack = [file_path.parents[0].iterdir()]
while stack:
    iterator = stack[-1]

    try:
        path: Path = next(iterator)
    except StopIteration:
        stack.pop()
        continue

    if path.name in exclude:
        continue

    if path.is_file():
        if path.suffix == '.py':
            with open(path) as file:
                for line in file:
                    for class_name in qt_regex.findall(line):
                        if class_name in ('py', 'constants'):
                            continue
                        class_object = getattr(qt, class_name)
                        import_info = class_object.__module__, class_name
                        imports.add(import_info)

    else:
        stack.append(path.iterdir())

with open('qt.py', 'w') as file:
    for package, module in imports:
        file.write(f'from {package} import {module}\n')

    file.write('\n')
    file.write('from PyQt5.QtCore import Qt as constants\n')
