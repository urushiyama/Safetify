#!/usr/bin/env python3

import functools
import inspect
from collections.abc import Callable
from typing import Any

def args_isolated(func) -> Callable[..., Any]:
    """Decolator to isolate arguments between inside and outside of the function.

    Returns the decorated function whose arguments are the copy of the original ones.
    """
    @functools.wraps(func)
    def isolated(*args, **kwargs):
        sig = inspect.signature(func)
        default_args = {k: v.default
                        for k, v in sig.parameters.items()
                        if v.default is not inspect.Parameter.empty}
        copied_args = list()
        copied_kwargs = dict()
        for arg in args:
            if hasattr(arg, 'copy'):
                copied_args.append(arg.copy())
            else:
                copied_args.append(arg)
        for key, value in kwargs.items():
            if hasattr(value, 'copy'):
                copied_kwargs[key] = value.copy()
            else:
                copied_kwargs[key] = value
        for key, value in default_args.items():
            if key in copied_kwargs.keys():
                continue
            if hasattr(value, 'copy'):
                copied_kwargs[key] = value.copy()
            else:
                copied_kwargs[key] = value
        result = func(*copied_args, **copied_kwargs)
        return result
    return isolated
