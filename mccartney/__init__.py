import abjad 

from .markups import *

def skip(*arguments, **keywords):
    return select().skip(*arguments, **keywords)


