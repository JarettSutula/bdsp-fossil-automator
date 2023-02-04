def add_indent_to_macro(macro):
    indent = "    "
    m = macro_to_list(macro)
    for i in range(len(m)):
        m[i] = indent + m[i]
    return m

def macro_to_list(macro):
    macro_list = macro.splitlines()
    # in macros.py, each macro starts with """\n for readibility.
    # unfortunately splitlines counts that as a line of an empty string. remove it.
    macro_list.pop(0)
    return macro_list