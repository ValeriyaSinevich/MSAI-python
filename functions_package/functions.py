# -*- coding: utf-8 -*-

class InvalideArgumentError(Exception):
    pass


def divide(a: int, b: int) -> float:
    if a == 0:
        raise InvalideArgumentError("can't divide by 0!")
    return a / b
