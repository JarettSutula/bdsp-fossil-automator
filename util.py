"""Contains functions to easily generator macros for text file."""

def add_indent_to_macro(macro):
    """Adds indent to all lines of a macro string, as NXBT loop requires
    an indent for the loop to work. Macros.py should not include indents
    as they may be required to be called without indents. Call helper function
    to move the text based macro (in text for readibility and modification)
    into list for easy write to a text file.
    """
    indent = "    "
    m = macro_to_list(macro)
    for i in range(len(m)):
        m[i] = indent + m[i]
    return m

def macro_to_list(macro):
    """Take in macro in string (separated) and put it into a list. Lists make
    text file creation easier as we don't have to deal with newline chars.
    """
    macro_list = macro.splitlines()
    # in macros.py, each macro starts with """\n for readibility.
    # unfortunately, splitlines counts that as a line of an empty string,
    # so it needs to be removed.
    macro_list.pop(0)
    return macro_list