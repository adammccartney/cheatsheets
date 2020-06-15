import collections
import itertools

import abjad 


class Expression(abjad.Expression):
    r"""
    Expression.
    ..  container:: example expression
        Transposes collections:
        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]
        >>> transposition = mccartney.Expression()
        >>> transposition = transposition.pitch_class_segment()
        >>> transposition = transposition.transpose(n=3)
        >>> expression = mccartney.sequence(name='J')
        >>> expression = expression.map(transposition)
        >>> for collection in expression(collections):
        ...     collection
        ...
        PitchClassSegment([3, 4, 5, 6])
        PitchClassSegment([9, 10, 11, 0])
        >>> expression.get_string()
        'T3(X) /@ J'
        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \line
                    {
                        \concat
                            {
                                T
                                \sub
                                    3
                                \bold
                                    X
                            }
                        /@
                        \bold
                            J
                    }
                }
    ..  container:: example expression
        Transposes and joins:
        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]
        >>> transposition = mccartney.Expression()
        >>> transposition = transposition.pitch_class_segment()
        >>> transposition = transposition.transpose(n=3)
        >>> expression = mccartney.sequence(name='J')
        >>> expression = expression.map(transposition)
        >>> expression = expression.join()
        >>> expression(collections)
        Sequence([PitchClassSegment([3, 4, 5, 6, 9, 10, 11, 0])])
        >>> expression.get_string()
        'join(T3(X) /@ J)'
        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \concat
                    {
                        join(
                        \line
                            {
                                \concat
                                    {
                                        T
                                        \sub
                                            3
                                        \bold
                                            X
                                    }
                                /@
                                \bold
                                    J
                            }
                        )
                    }
                }
    ..  container:: example expression
        Transposes and flattens:
        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]
        >>> transposition = mccartney.Expression()
        >>> transposition = transposition.pitch_class_segment()
        >>> transposition = transposition.transpose(n=3)
        >>> expression = mccartney.sequence(name='J')
        >>> expression = expression.map(transposition)
        >>> expression = expression.flatten(depth=-1)
        >>> for collection in expression(collections):
        ...     collection
        ...
        NumberedPitchClass(3)
        NumberedPitchClass(4)
        NumberedPitchClass(5)
        NumberedPitchClass(6)
        NumberedPitchClass(9)
        NumberedPitchClass(10)
        NumberedPitchClass(11)
        NumberedPitchClass(0)
        >>> expression.get_string()
        'flatten(T3(X) /@ J, depth=-1)'
        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \concat
                    {
                        flatten(
                        \line
                            {
                                \concat
                                    {
                                        T
                                        \sub
                                            3
                                        \bold
                                            X
                                    }
                                /@
                                \bold
                                    J
                            }
                        ", depth=-1)"
                    }
                }
    ..  container:: example expression
        Transposes and repartitions:
        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]
        >>> transposition = mccartney.pitch_class_segment().transpose(n=3)
        >>> expression = mccartney.sequence(name='J').map(transposition)
        >>> expression = expression.flatten(depth=-1).partition([3])
        >>> expression = expression.pitch_class_segments()
        >>> for collection in expression(collections):
        ...     collection
        ...
        PitchClassSegment([3, 4, 5])
        PitchClassSegment([6, 9, 10])
        PitchClassSegment([11, 0])
        >>> expression.get_string()
        'X /@ P[3](flatten(T3(X) /@ J, depth=-1))'
        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \line
                    {
                        \bold
                            X
                        /@
                        \concat
                            {
                                P
                                \sub
                                    [3]
                                \concat
                                    {
                                        flatten(
                                        \line
                                            {
                                                \concat
                                                    {
                                                        T
                                                        \sub
                                                            3
                                                        \bold
                                                            X
                                                    }
                                                /@
                                                \bold
                                                    J
                                            }
                                        ", depth=-1)"
                                    }
                            }
                    }
                }
    ..  container:: example expression
        Transposes, repartitions and ox-plows:
        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]
        >>> transposition = mccartney.pitch_class_segment().transpose(n=3)
        >>> expression = mccartney.sequence(name='J').map(transposition)
        >>> expression = expression.flatten(depth=-1).partition([3])
        >>> expression = expression.pitch_class_segments()
        >>> expression = expression.boustrophedon()
        >>> for collection in expression(collections):
        ...     collection
        ...
        PitchClassSegment([3, 4, 5])
        PitchClassSegment([6, 9, 10])
        PitchClassSegment([11, 0])
        PitchClassSegment([11])
        PitchClassSegment([10, 9, 6])
        PitchClassSegment([5, 4, 3])
        >>> expression.get_string()
        'β2(X /@ P[3](flatten(T3(X) /@ J, depth=-1)))'
        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \concat
                    {
                        β
                        \super
                            2
                        \line
                            {
                                \bold
                                    X
                                /@
                                \concat
                                    {
                                        P
                                        \sub
                                            [3]
                                        \concat
                                            {
                                                flatten(
                                                \line
                                                    {
                                                        \concat
                                                            {
                                                                T
                                                                \sub
                                                                    3
                                                                \bold
                                                                    X
                                                            }
                                                        /@
                                                        \bold
                                                            J
                                                    }
                                                ", depth=-1)"
                                            }
                                    }
                            }
                    }
                }
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = "Classes"

    ### PRIVATE METHODS ###

    def _evaluate_accumulate(self, *arguments):
        assert len(arguments) == 1, repr(arguments)
        globals_ = self._make_globals()
        assert "__argument_0" not in globals_
        __argument_0 = arguments[0]
        assert isinstance(__argument_0, Sequence), repr(__argument_0)
        class_ = type(__argument_0)
        operands = self.map_operand
        globals_["__argument_0"] = __argument_0
        globals_["class_"] = class_
        globals_["operands"] = operands
        statement = "__argument_0.accumulate(operands=operands)"
        try:
            result = eval(statement, globals_)
        except (NameError, SyntaxError, TypeError) as e:
            raise Exception(f"{statement!r} raises {e!r}.")
        return result

    ### PUBLIC METHODS ###

    def pitch_class_segment(self, **keywords) -> "Expression":
        r"""
        Makes pitch-class segment subclass expression.
        ..  container:: example
            Makes expression to apply alpha transform to pitch-class segment:
            >>> mccartney.PitchClassSegment([-2, -1.5, 6, 7, -1.5, 7])
            PitchClassSegment([10, 10.5, 6, 7, 10.5, 7])
            >>> segment = mccartney.PitchClassSegment([-2, -1.5, 6, 7, -1.5, 7])
            >>> abjad.show(segment, strict=89) # doctest: +SKIP
            ..  container:: example expression
                >>> expression = mccartney.Expression(name='J')
                >>> expression = expression.pitch_class_segment()
                >>> expression = expression.alpha()
                >>> expression([-2, -1.5, 6, 7, -1.5, 7])
                PitchClassSegment([11, 11.5, 7, 6, 11.5, 6])
                >>> segment = expression([-2, -1.5, 6, 7, -1.5, 7])
                >>> markup = expression.get_markup()
                >>> abjad.show(segment, figure_name=markup) # doctest: +SKIP
                ..  docs::
                    >>> lilypond_file = segment.__illustrate__(
                    ...     figure_name=markup,
                    ...     )
                    >>> abjad.f(lilypond_file[abjad.Staff])
                    \new Staff
                    {
                        \new Voice
                        {
                            b'8
                            ^ \markup {
                                \concat
                                    {
                                        A
                                        \bold
                                            J
                                    }
                                }
                            bqs'8
                            g'8
                            fs'8
                            bqs'8
                            fs'8
                            \bar "|." %! SCORE_1
                            \override Score.BarLine.transparent = ##f
                        }
                    }
        """
        from .pitchclasses import PitchClassSegment

        class_ = PitchClassSegment
        callback = self._make_initializer_callback(
            class_, module_names=["mccartney"], string_template="{}", **keywords
        )
        expression = self.append_callback(callback)
        return abjad.new(expression, proxy_class=class_)

    def pitch_class_segments(self) -> "Expression":
        """
        Maps pitch-class segment subclass initializer to expression.
        """
        initializer = Expression().pitch_class_segment()
        return self.map(initializer)

    def select(self, **keywords) -> "Expression":
        r"""
        Makes select expression.
        ..  container:: example
            Makes expression to select leaves:
            ..  container:: example
                >>> staff = abjad.Staff()
                >>> staff.extend("<c' bf'>8 <g' a'>8")
                >>> staff.extend("af'8 r8")
                >>> staff.extend("r8 gf'8")
                >>> abjad.attach(abjad.TimeSignature((2, 8)), staff[0])
                >>> abjad.show(staff, strict=89) # doctest: +SKIP
                ..  docs::
                    >>> abjad.f(staff, strict=89)
                    \new Staff
                    {
                        \time 2/8
                        <c' bf'>8
                        <g' a'>8
                        af'8
                        r8
                        r8
                        gf'8
                    }
            ..  container:: example expression
                >>> expression = mccartney.Expression()
                >>> expression = expression.select()
                >>> expression = expression.leaves()
                >>> for leaf in expression(staff):
                ...     leaf
                ...
                Chord("<c' bf'>8")
                Chord("<g' a'>8")
                Note("af'8")
                Rest('r8')
                Rest('r8')
                Note("gf'8")
        """
        class_ = Selection
        callback = self._make_initializer_callback(
            class_, module_names=["mccartney"], **keywords
        )
        expression = self.append_callback(callback)
        return abjad.new(expression, proxy_class=class_, template="mccartney")

    def sequence(self, **keywords) -> "Expression":
        """
        Makes sequence expression.
        """
        name = keywords.pop("name", None)
        expression = Expression(name=name)
        callback = expression._make_initializer_callback(
            Sequence, module_names=["mccartney"], string_template="{}", **keywords
        )
        expression_ = expression.append_callback(callback)
        return abjad.new(expression_, proxy_class=Sequence)

class Selection(abjad.Selection):
    """
    Selection.
    ..  container:: example
        >>> baca.select()
        baca
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = "Classes"

    __slots__ = ()

    ### PUBLIC METHODS ###

    def chead(
        self, n: int, *, exclude: abjad.Strings = None
    ) -> typing.Union[abjad.Note, abjad.Expression]:
        r"""
        Selects chord head ``n``.
        ..  container:: example
            Selects chord head -1:
            ..  container:: example
                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.setting(staff).auto_beaming = False
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP
                >>> result = baca.select(staff).chead(-1)
                >>> result
                Chord("<fs' gs'>4")
            ..  container:: example expression
                >>> selector = baca.chead(-1)
                >>> result = selector(staff)
                >>> selector.print(result)
                Chord("<fs' gs'>4")
                >>> selector.color(result)
                >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP
            ..  docs::
                >>> abjad.f(staff, strict=89)
                \new Staff
                \with
                {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                    autoBeaming = ##f
                }
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 10/9 {
                        r16
                        bf'16
                        <a'' b''>16
                        c'16
                        <d' e'>4
                        ~
                        <d' e'>16
                    }
                    \times 8/9 {
                        r16
                        bf'16
                        <a'' b''>16
                        d'16
                        <e' fs'>4
                        ~
                        <e' fs'>16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 10/9 {
                        r16
                        bf'16
                        <a'' b''>16
                        e'16
                        \abjad-color-music #'green
                        <fs' gs'>4
                        ~
                        <fs' gs'>16
                    }
                }
        """
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.cheads(exclude=exclude)[n]
