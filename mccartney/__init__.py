import abjad 

from .classes import *
from .commands import *
from .markups import *
from .segments import *

def skip(*arguments, **keywords):
    return select().skip(*arguments, **keywords)


