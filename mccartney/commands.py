import inspect
import typing

import abjad

def select(items=None):
    if items is None:
        return classes.Expression().select()
    return classes.Selection(items=items)
