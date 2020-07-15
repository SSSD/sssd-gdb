def PrettyPrinterType(type_name):
    """
    Creates GDB Pretty Printer.

    :param type_name: Type name that should be registered with this printer.
    :type type_name: string
    """
    def decorator(cls):
        cls._gdb_pp_type = type_name
        return cls

    return decorator

def PrettyPrinterGroup(group_name):
    """
    Creates GDB Pretty Printer group.

    :param group_name: Group name.
    :type group_name: string
    """
    def decorator(cls):
        cls._gdb_pp_group = group_name
        return cls

    return decorator
