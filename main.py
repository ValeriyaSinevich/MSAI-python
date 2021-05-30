# -*- coding: utf-8 -*-

from import_monster import aa_module, bb_module, methods_importer

if __name__ == '__main__':
    print(
        methods_importer(
            'aa_method', ['import_monster.aa_module', bb_module, aa_module]
        )
    )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
