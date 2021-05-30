
from import_monster import methods_importer, aa_module, bb_module
from typing import List, Union
from types import ModuleType


if __name__ == '__main__':
    print(methods_importer('aa_method', ['import_monster.aa_module', bb_module, aa_module]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
