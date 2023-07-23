import os
from enum import StrEnum, auto


class Env(StrEnum):
    DEV = auto()
    ALPHA = auto()
    BETA = auto()
    STAGING = auto()
    PRODUCTION = auto()


CURRENT_ENV = Env(os.getenv("env", Env.DEV))
