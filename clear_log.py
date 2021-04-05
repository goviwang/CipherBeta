from os import system, name

def clear():
    """
    This function will clear the python shell
    for windows and mac.
    """
    # Windows Os.
    if name == "nt":
        _ = system ("cls")
    # Mac Os
    else:
        _ = system ("clear")
