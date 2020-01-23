def f(a,):
    ...

def f(a:int=1,):
    ...

def xxxxxxxxxxxxxxxxxxxxxxxxxxxx() -> Set[
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]:
    pass

def _gopass_process() -> Popen:
    """Spawn a Gopass process"""
    return Popen(
        ['gopass', 'jsonapi', 'listen'],
        stdout=PIPE,
        stdin=PIPE,
    )

# output

def f(a):
    ...


def f(a: int = 1):
    ...


def xxxxxxxxxxxxxxxxxxxxxxxxxxxx() -> Set[
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]:
    pass


def _gopass_process() -> Popen:
    """Spawn a Gopass process"""
    return Popen(["gopass", "jsonapi", "listen"], stdout=PIPE, stdin=PIPE)
