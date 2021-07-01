import random

from .words import PREFIXES, SUFFIXES


def generate(case: str = "camel") -> str:
    prefix = random.choice(PREFIXES)
    suffix = random.choice(SUFFIXES)
    if case == "camel":
        nickname = f"{prefix}{suffix}"
    elif case == "snake":
        nickname = f"{prefix.lower()}_{suffix.lower()}"
    else:
        raise ValueError('case must be either "camel" or "snake"')
    return nickname
