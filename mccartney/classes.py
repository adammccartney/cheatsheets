import abjad 


class PitchDeck(object):
    """
    PitchDeck takes a list of PitchSegments
    It stores these in a "deck" - list of PitchSegments
    where the indexes have vertical relationships
    """
    def __init__(self, pitch_segments=[]):
        self._pitch_segments = pitch_segments

    def __call__(self):
        return self 

    def get_pitch_segments(self):
        "Returns a list of pitch segments"
        return self._pitch_segments

    def transpose(self, n=0):
        r"""
        Transposes every pitch segment by index `n`.
        Returns a new instance of PitchDeck
        """
        
        segments = self.get_pitch_segments()
        transposed_segments = []
        if isinstance(segments, list):
            for segment in segments:
                transposed_segments.append(segment.transpose(n))
            transposed_pitch_deck = PitchDeck(transposed_segments)
            return transposed_pitch_deck


