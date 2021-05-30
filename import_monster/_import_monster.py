from collections.abc import Callable
from typing import List, Union
from types import ModuleType
import importlib

def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    found_methods = set()
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError('Must be list of strings or ModuleType')
            method = getattr(mod, method_name, None)
            if method:
                found_methods.add(method)
        except ImportError:
            continue
    return list(found_methods)
