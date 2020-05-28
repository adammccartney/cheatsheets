import inspect
import typing

import abjad

# method for inverting chords
def invertChord(chord, inv):
    invertedChord = abjad.Chord()
    _chord = chord.__copy__()
    if isinstance(chord, abjad.Chord):
        for i in range(inv):
            noteList = _chord.note_heads               # copy noteheads to new list 
            lowestNoteHead = noteList.pop(0)          # get lowest note_head
            lowestPitch = lowestNoteHead.named_pitch  # note_head to pitch
            highestPitch = lowestPitch.transpose(12)  # transpose up an octave
            highestNoteHead = abjad.NoteHead(highestPitch.name) # Pitch to NoteHead
            newNoteList = noteList[0::]               # make new list of upper tones
            newNoteList.append(highestNoteHead)       # append notehead to list
            _chord.note_heads = newNoteList           # reset _chord with permuted list
            # print(_chord)
        return _chord                                 # return target inversion

