# To Do re:abjad

# Write concrete SegmentMaker class

In abjad, SegmentMaker refers to an abstract factory used as the base class for
all segments created during the composition of a score. Every new score
repository therefor, needs to contain a concrete factors of the same name, that
overrides methods in the base class.

The simplest possible definition of a SegmentMaker (i.e. the simplest way to
get some notation on the screen is:

```
import abjad

class SegmentMaker(abjad.SegmentMaker):
    """Defines concrete factory class Segment-maker"""

    def _make_lilypond_file(self, midi=False):
        return abjad.Staff("c'4 d'4 e'4 f'4").__illustrate__()
```

# Private members

A segment maker has some private members and methods that are essential aspects
of the classes functionality. These include (at least) \_metadata and \_score

# private properties

@property
is:

- a function decorator
- runtime declaration about the function that follows
- used to implement the concrete SegmentMaker,
  specfically the instruments used by the score (and therefor every instance of a
  segment) become private properties of the segment maker class.
  This means that they are a type of static member and are not associated with
  any particular object, therefor cannot be accessed from an instance.

# check out static and class methods

there are some interesting capacities here with both of these types of method.
For instance, it is possible to define a static method that returns number of
instances of a class. (see lutz, learning python p1031)

# _there are some intricacies with Class methods, follow up here!_

# Strategy for defining a SegmentMaker

In the definition of a score's ScoreTemplate,
a private member \_voice_abbreviations is defined in the **slots** class variable
is initialized as an abjad.OrderedDict()

the ScoreTemplate definition then populates this dictionary with pairs in the
form -  
`"In.": "Instrument_Music_Voice"`

To Do:

- write a little generator that takes an abjad.OrderedDict() of
  voice_abbreviations and makes a ScoreTemplate
- also used same OrderedDict to set the static variables (@property) of the
  SegmentMaker

- Learn about testing with test.py and travis ci
