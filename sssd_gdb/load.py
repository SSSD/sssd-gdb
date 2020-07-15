import inspect
import os
import pkgutil
import sys

# GDB does not know about the module location so we need to add it to python
# paths so GDB is able to resolve our modules.
path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/..')
sys.path.append(path)

import gdb.printing
import sssd_gdb.printers


pkgs = pkgutil.walk_packages(
    sssd_gdb.printers.__path__,
    sssd_gdb.printers.__name__ + '.'
)

for m in pkgs:
    m.module_finder.find_module(m.name).load_module(m.name)

def register_group(group_obj):
    pp = gdb.printing.RegexpCollectionPrettyPrinter(group_obj._gdb_pp_group)
    for _, obj in inspect.getmembers(group_obj):
        if inspect.isclass(obj):
            if hasattr(obj, '_gdb_pp_type'):
                pp.add_printer(obj._gdb_pp_type, f'^{obj._gdb_pp_type}$', obj)
            elif issubclass(obj, sssd_gdb.printers.PrettyPrinter):
                pp.add_printer(obj.__name__, f'^{obj.__name__}$', obj)

    return pp

def load_printers():
    modules = [x for x in sys.modules if x.startswith('sssd_gdb.printers.')]
    for module in modules:
        for _, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj) and hasattr(obj, '_gdb_pp_group'):
                pp = register_group(obj)
                gdb.printing.register_pretty_printer(gdb.current_objfile(), pp)

load_printers()
