# Streams and Patterns

Patterns define behavior; streams execute it

Patterns are the basic layout of a musical piece, we write streams to exectute
on the plan / score described by the patterns. 

**Patterns are stateless**


```
a = Pseries(start: 0, step: 1, length: inf).asStream;
a.nextN(10);

b = a.asStream;
b.next;

c = a.asStream;
c.next; // starts from zero

b.next; // continues from where it was before

[b.next, c.next];
```

## Primary Patterns 

### Pseq(list, repeats, offset)
    Play through the entire list repeats times. Like list.do.
### Prand(list, repeats)
    Choose items from the list randomly (same as list.choose).
### Pxrand(list, repeats)
    Choose randomly, but never repeat the same item twice in immediate succession.
### Pshuf(list, repeats)
    Shuffle the list in random order, and use the same random order repeats times. Like list.scramble.
### Pwrand(list, weights, repeats)
    Choose randomly, according to weighted probabilities (same as list.wchoose(weights)).
### Pseries(start, step, length)
    Arithmetic series (addition).
### Pgeom(start, grow, length)
    Geometric series (multiplication).
### Pwhite(lo, hi, length)
    Random numbers, equal distribution ("white noise"). Like rrand(lo, hi) .
### Pexprand(lo, hi, length)
    Random numbers, exponential distribution. Like exprand(lo, hi) .
### Pbrown(lo, hi, step, length)
    Brownian motion, arithmetic scale (addition).
### Pfunc(nextFunc, resetFunc)
    Get the stream values from a user-supplied function.
### Pfuncn(func, repeats)
    Get values from the function, but stop after repeats items.
### Prout(routineFunc)
    Use the function like a routine. The function should return values using .yield or .embedInStream.

## Additional List Patterns

### Pser(list, repeats, offset)
    Play through the list as many times as needed, but output only repeats items.
### Pslide(list, repeats, len, step, start, wrapAtEnd)
    Play overlapping segments from the list.
### Pwalk(list, stepPattern, directionPattern, startPos)
    Random walk over the list.
### Place(list, repeats, offset)
    Interlace any arrays found in the main list.
### Ppatlace(list, repeats, offset)
    Interlace any patterns found in the main list.
### Ptuple(list, repeats)
    Collect the list items into an array as the return value.

## Additional Random Number Generators

### Pgbrown(lo, hi, step, length)
    Brownian motion, geometric scale (multiplication).
### Pbeta(lo, hi, prob1, prob2, length)
    Beta distribution, where prob1 = α (alpha) and prob2 = β (beta).
### Pcauchy(mean, spread, length)
    Cauchy distribution.
### Pgauss(mean, dev, length)
    Guassian (normal) distribution.
### Phprand(lo, hi, length)
    Returns the greater of two equal-distribution random numbers.
### Plprand(lo, hi, length)
    Returns the lesser of two equal-distribution random numbers.
### Pmeanrand(lo, hi, length)
    Returns the average of two equal-distribution random numbers, i.e., (x + y) / 2.
### Ppoisson(mean, length)
    Poisson distribution.
### Pprob(distribution, lo, hi, length, tableSize)
    Arbitrary distribution, based on a probability table.

## Simple sequential and random patterns 

`Pseq` and `Pser` can be used to create sequential patterns that move along
linearly. The thing to note is that Pbind takes a number of tuples as
arguments, in the format *\function, Values* where values can be a single value
or a list of value arguments. 

```
// Flock of Seagulls!
(
p = Pbind(
    \degree, Pslide((-6, -4 .. 12), 8, 3, 1, 0),
    \dur, Pseq(#[0.1, 0.1, 0.2], inf),
    \sustain, 0.15
).play;
)


// Pwrand: these probabilities favor triadic notes from scale degrees
(
p = Pbind(
    \degree, Pwrand((0..7), [4, 1, 3, 1, 3, 2, 1].normalizeSum, inf),
    \dur, Pseq(#[0.1, 0.1, 0.2, 0.5, 1], inf),
).play;
)
```

## Interlacing values and making arrays

```

// Hanon exercise
(
p = Pbind(
    \degree, Ppatlace([
        Pseries(0, 1, 8),    // first, third etc. notes
        Pseries(2, 1, 7)    // second, fourth etc. notes
    ], inf),
    \dur, 0.25
).play;
)

// Chords
// \degree receives [7, 9, 4], then [6, 7, 4] successively, expanded to chords on the server
(
p = Pbind(
    \degree, Ptuple([
        Pseries(7, -1, 8),
        Pseq([9, 7, 7, 7, 4, 4, 2, 2], 1),
        Pseq([4, 4, 4, 2, 2, 0, 0, -3], 1)
    ], 1),
    \dur, 1
).play;
)
```

## Pbind info

Pbind is the central class for musical sequences, it must be turned into a
stream of course...

A Pbind stream is made up of Events. An Event is a subclass of a Dictionary.
Therefor Pbind definitions are essentially key[value] pairs like a dictionary.

```
e = (freq: 440, dur: 0.5);    // an Event

e.at(\freq)        // access a value by name
e[\freq]
e.freq        // See IdentityDictionary help for more on this usage

e.put(\freq, 880);    // Change a value by name
e[\freq] = 660;
e.freq = 220;

e.put(\amp, 0.6);    // Add a new value into the event
e.put(\dur, nil);    // Remove a value
```

Furthermore: dictionaries in Supercollider are unordered patterns, even though
Pbind processes its child streams in the order given, the results can display
the keys and values in any order.


### Events to control SynthDef

most SynthDefs have control inputs that are possible to control using events

```
SynthDef(\harpsi, { |outbus = 0, freq = 440, amp = 0.1, gate = 1|
    var out;
    out = EnvGen.ar(Env.adsr, gate, doneAction: Done.freeSelf) * amp *
        Pulse.ar(freq, 0.25, 0.75);
    Out.ar(outbus, out ! 2);
}).add;    // see below for more on .add

p = Pbind(
        // Use \harpsi, not \default
    \instrument, \harpsi,
    \degree, Pseries(0, 1, 8),
    \dur, 0.25
).play;
```

### Rest events

```
(
// first, pitches ascending by 1-3 semitones, until 2 octaves are reached
var    pitches = Pseries(0, Pconst(24, Pwhite(1, 3, inf)), inf).asStream.all,
        // randomly block 1/3 of those
    mask = pitches.scramble[0 .. pitches.size div: 3];

p = Pbind(
    \arpeg, Pseq(pitches[ .. pitches.size - 2] ++ pitches.reverse[ .. pitches.size - 2], inf),
        // if the note is found in the mask array, replace it with Rest
        // then that note does not sound
    \note, Pif(Pfunc { |event| mask.includes(event[\arpeg]) }, Rest(0), Pkey(\arpeg)),
    \octave, 4,
    \dur, 0.125
).play;
)

p.stop;
```

### Argument name prefixes
Initial arguments to synth defs are specified as follows:
+ t_ trigger event
+ i_ initial rate
